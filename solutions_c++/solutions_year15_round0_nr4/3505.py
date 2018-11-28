#include<iostream>

using namespace std;

int main(){
	int T;
	int X, R, C;
	int rInt;
	char result[8];

	FILE *fi, *fo;

	fopen_s(&fi, "D-small-attempt7.in", "r");
	fopen_s(&fo, "output.txt", "w");

	fscanf_s(fi, "%d", &T);

	for (int i = 0; i < T; i++){
		rInt = 0;
		fscanf_s(fi, "%d", &X);
		fscanf_s(fi, "%d", &R);
		fscanf_s(fi, "%d", &C);

		switch (X){
		case 1:
			rInt = 1;
			break;
		case 2:
			if (((R*C) % 2 == 0))
				rInt = 1;
			else
				rInt = 0;
			break;
		case 3:
			if ((R*C) % 3 == 0 && ((R >= 3 && C >= 2) || (R >= 2 && C >= 3)))
				rInt = 1;
			else
				rInt = 0;
			break;
		case 4:
			if ((R*C) % 4 == 0 && ((R >= 4 && C >= 3) || (R >= 3 && C >= 4)))
				rInt = 1;
			else
				rInt = 0;
			break;
		case 5:
			rInt = 0;
			break;
		case 6:
			rInt = 0;
			break;
		default:
			rInt = 0;
			break;
		}

		if (rInt){
			strcpy_s(result, "GABRIEL");
		}
		else {
			strcpy_s(result, "RICHARD");
		}
		fprintf(fo, "Case #%d: %s\n", i + 1, result);
	}
	return 0;
}