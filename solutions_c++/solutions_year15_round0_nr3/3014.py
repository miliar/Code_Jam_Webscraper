// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

class icomplex {
public:
	int real;
	int imag;

	icomplex(): real(0), imag(0) {}

	icomplex(int r, int i): real(r), imag(i) {}

	icomplex operator +(const icomplex &a) {
		icomplex Out;
		Out.real = real + a.real;
		Out.imag = imag + a.imag;
		return Out;
	}

	icomplex operator *(const icomplex &a) {
		icomplex Out;
		Out.real = real*a.real - imag*a.imag;
		Out.imag = real*a.imag + imag*a.real;
		return Out;
	}

	bool operator !=(const icomplex &a) {
		if ((real != a.real) || (imag != a.imag)) 
			return true;
		else
			return false;
	}
};

class cmat22 {
public:
	//  a[0]   a[1]
	//
	//	a[2]   a[3]
	icomplex a[4];
 
	cmat22() {}

	cmat22(int w, int x, int y, int z) {
		a[0] = icomplex(w, -z);
		a[1] = icomplex(-y, -x);
		a[2] = icomplex(y, -x);
		a[3] = icomplex(w, z);
	}

	cmat22 operator +(const cmat22 M) {
		cmat22 Out;
		Out.a[0] = a[0] + M.a[0];
		Out.a[1] = a[1] + M.a[1];
		Out.a[2] = a[2] + M.a[2];
		Out.a[3] = a[3] + M.a[3];
		return Out;
	}

	cmat22 operator *(const cmat22 M) {
		cmat22 Out;
		Out.a[0] = a[0]*M.a[0] + a[1]*M.a[2];
		Out.a[1] = a[0]*M.a[1] + a[1]*M.a[3];
		Out.a[2] = a[2]*M.a[0] + a[3]*M.a[2];
		Out.a[3] = a[2]*M.a[1] + a[3]*M.a[3];
		return Out;
	}

	bool operator ==(const cmat22 M) {
		if (a[0] != M.a[0]) return false;
		if (a[1] != M.a[1]) return false;
		if (a[2] != M.a[2]) return false;
		if (a[3] != M.a[3]) return false;
		return true;
	}
};

cmat22 Identity(1, 0, 0, 0);
cmat22 PauliX(0, 1, 0, 0);
cmat22 PauliY(0, 0, 1, 0);
cmat22 PauliZ(0, 0, 0, 1);

typedef struct sTestCase {
	int StringLength;
	int Repetitions;
	char Str[16384];
} sTestCase;

bool ProcessTestCase(sTestCase Case) {

	// Create matrix
	cmat22 Mat = Identity;

	// Compute substep matrix
	for (int i=0; i<Case.StringLength; ++i) {
		switch (Case.Str[i]) {
		case 'i':
			Mat = Mat * PauliX;
			break;
		case 'j':
			Mat = Mat * PauliY;
			break;
		case 'k':
			Mat = Mat * PauliZ;
			break;
		}
	}

	// Compute the k-th power of the matrix
	cmat22 PowerMat = Identity;
	for (int i=0; i<Case.Repetitions; ++i) {
		PowerMat = PowerMat * Mat;
	}

	// Test
	cmat22 Comparison = PauliX * PauliY * PauliZ;
	if (!(PowerMat == Comparison))
		return false; // Wrong product of matrices
	
	// Test other possibilities
	if (Case.Repetitions*Case.StringLength < 3)
		return false;

	// Search X from left
	int XFound = -1;
	Mat = Identity;
	for (int i=0; i<Case.Repetitions; ++i) {
		for (int j=0; j<Case.StringLength; ++j) {
			switch (Case.Str[j]) {
			case 'i':
				Mat = Mat * PauliX;
				break;
			case 'j':
				Mat = Mat * PauliY;
				break;
			case 'k':
				Mat = Mat * PauliZ;
				break;
			}
			if (Mat == PauliX) {
				XFound = (i*Case.StringLength)+j;
				goto wend;
			}
		}
	}
wend:
	// Test if X Found
	if (XFound == -1) 
		return false;

	// Search Z from right
	int ZFound = -1;
	Mat = Identity;
	for (int i=Case.Repetitions-1; i>=0; --i) {
		for (int j=Case.StringLength-1; j>=0; --j) {
			switch (Case.Str[j]) {
			case 'i':
				Mat = PauliX * Mat;
				break;
			case 'j':
				Mat = PauliY * Mat;
				break;
			case 'k':
				Mat = PauliZ * Mat;
				break;
			}
			if (Mat == PauliZ) {
				ZFound = (i*Case.StringLength)+j;
				goto wend2;
			}
		}
	}
wend2:
	// Test if X Found
	if (ZFound == -1) 
		return false;

	// Test found positions if Y can exist
	if (ZFound <= XFound) 
		return false;

	// Return
	return true;
}

int main(int argc, char* argv[]) {
	if (argc == 1) {
		return 1;
	}

	// Open file
	FILE *InputFile = NULL;
	FILE *OutputFile = NULL;
	InputFile = fopen(argv[1], "r");
	OutputFile = fopen("out.txt", "w");

	// Read cases
	int TestCases = 0;
	printf("Processing %s ... \n", argv[1]);
	int Read = fscanf(InputFile, "%i\n", &TestCases);
	if (Read != 1) {
		return 1;
	}

	// Cycle on cases
	char LineBuf[4096];
	int StringLength = 0, Repetitions = 0;
	for (int i=0; i<TestCases; ++i) {
		sTestCase Case;
		memset((void *)&Case, 0, sizeof(sTestCase));

		// Read settings
		fscanf(InputFile, "%i %i\n", &Case.StringLength, &Case.Repetitions);

		// Read line
		fgets(Case.Str, 16384, InputFile);

		// Call process test case
		bool CanDecompose = ProcessTestCase(Case);

		// Print
		if (CanDecompose) {
			printf("Case #%i: YES\n", i+1);
			fprintf(OutputFile, "Case #%i: YES\n", i+1);
		} else {
			printf("Case #%i: NO\n", i+1);
			fprintf(OutputFile, "Case #%i: NO\n", i+1);
		}
	}

	// Close file
	fclose(InputFile);
	fclose(OutputFile);
	_getch();

	return 0;
}

