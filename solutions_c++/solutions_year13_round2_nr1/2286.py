#include <iostream.h>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <algorithm>

#define INFILE	"A-small-attempt2.in"
#define OUTFILE	"A-small-attempt2.out"
#define DATA_MAX_LENGTH 18

using namespace std;

class BigNumStr {
public:
	string m_strNum;
	bool m_blEnd;
	void AddBigNum(string strAddNum);
	void AssignBigNum(string strNum);
	string GetBigBum();
};

void BigNumStr::AddBigNum(string strAddNum)
{
//	printf("%s + %s.\n", strAddNum.c_str(), m_strNum.c_str());
	reverse(strAddNum.begin(), strAddNum.end());
	int MaxNumLength = (m_strNum.length() > strAddNum.length()) ? m_strNum.length() : strAddNum.length();
	int LengthDiff = 0;
	int A, B, Sum;
	bool blCarry = false; 
	
	LengthDiff = m_strNum.length() - strAddNum.length();
//	printf("LengthDiff = %d\n", LengthDiff);
	if (0 < LengthDiff) {
		for (int i=0; i<LengthDiff; i++) {
			strAddNum += "0";
		}
	} else {
		for (int i=0; i<-1*LengthDiff; i++) {
			m_strNum +=  "0";
		}
	}
	
//	printf("%s + %s.\n", strAddNum.c_str(), m_strNum.c_str());
	
	for (int i=0; i<MaxNumLength; i++){
		A = m_strNum[i] - '0';
		B = strAddNum[i] - '0';
		Sum = A + B;
		if (true == blCarry) {
			Sum++;
		}
		
		if ((19 <= Sum) || (0 > Sum)) {
			printf("[BigNumStr::Add] : Error sum detected. A = %d, B = %d, At [%d]. Sum [%d].\n",  A, B, i, Sum);
			return; 
		}

//		printf("[BigNumStr::Add] : A = %d, B = %d, At [%d]. Sum [%d].\n", A, B, i, Sum);

		if (10 <= Sum) {
			m_strNum[i] = '0' + Sum - 10;
			blCarry = true;
		} else {
			m_strNum[i] = '0' + Sum;
			blCarry = false;
		}
	}

	return;
}

void BigNumStr::AssignBigNum(string strNum)
{
	m_blEnd = false;
	m_strNum = strNum;
	reverse(m_strNum.begin(), m_strNum.end());
	return;
}

string BigNumStr::GetBigBum()
{
	string strNum = m_strNum;
	reverse(strNum.begin(), strNum.end());
	return strNum;	
}

int GetVals(FILE *infile, int* pVals, int Length, bool blInLine = false)
{
	char CurChar;
	
	if (0 == Length) {
		printf("[GetVals] : Illegal length\n");
		return -1;
	}
	if (NULL == pVals) {
		printf("[GetVals] : Illegal pVals\n");
		return -1;
	}

	for (int i=0; i < Length; i++) {
		pVals[i] = 0;
		
		int LoopCnt =0;
		CurChar = fgetc(infile);
		while ((EOF != CurChar) && 
  			   ('\n' != CurChar) &&
 			   (' ' != CurChar)) {
 			//printf("%c\n", CurChar);
 			//printf("=> %d, %d\n",pVals[i], (CurChar - '0'));
 			pVals[i] = pVals[i] * 10 + (CurChar - '0');
 			//printf("==> %d\n",pVals[i]);
 			
 			LoopCnt++;
 			if (DATA_MAX_LENGTH <= LoopCnt) {
 				printf("[GetVals] : DATA_MAX_LENGTH error detected.\n");
				return -1;
 			}
 			
 			CurChar = fgetc(infile);
 			if (blInLine && ('\n' == CurChar) && ((Length - 1) != i)) {
 				pVals[i+1] = -1;
 				return 0;
 			}
		}
	}
	
	return 0;
}

int GetBigVals(FILE *infile, BigNumStr* pVals, int Length, bool blInLine = false)
{
	char CurChar;
	string CurString;
	
	if (0 == Length) {
		printf("[GetVals] : Illegal length\n");
		return -1;
	}
	if (NULL == pVals) {
		printf("[GetVals] : Illegal pVals\n");
		return -1;
	}

	for (int i=0; i < Length; i++) {
		CurString = "";

		int LoopCnt =0;
		CurChar = fgetc(infile);
		while ((EOF != CurChar) && 
  			   ('\n' != CurChar) &&
 			   (' ' != CurChar)) {
 			CurString += CurChar;
 			
 			LoopCnt++;
 			if (DATA_MAX_LENGTH <= LoopCnt) {
 				printf("[GetVals] : DATA_MAX_LENGTH error detected.\n");
				return -1;
 			}
 			
 			CurChar = fgetc(infile);
 			if (blInLine && ('\n' == CurChar) && ((Length - 1) != i)) {
 				pVals[i].AssignBigNum(CurString);
 				pVals[i+1].m_blEnd = true;
 				return 0;
 			}
		}
		pVals[i].AssignBigNum(CurString);
	}
	
	return 0;
}

void Swap(int& A, int& B)
{
	int Tmp = A;
	A = B;
	B = Tmp;
	return;	
}

void Sort(int* pInt, int Length)
{
	bool blChanged = true;
	
	while (true == blChanged) {
		blChanged = false;
		for (int i=0; i<Length-1; i++) {
			if (pInt[i] > pInt[i+1]) {
				Swap(pInt[i], pInt[i+1]);
				blChanged = true;
			}
		}
	}
	
	return;
}

int main(int argc, char *argv[])
{
	FILE *infile, *outfile;
	int i = 0, j = 0, k = 0;
	char CurChar;
	string pStr[10];
	int NumOfGame = 0;

	if ( (infile = fopen(INFILE, "r")) == NULL ) {
		printf("can't open input file\n");
//		return -1;
	} else if( (outfile = fopen(OUTFILE, "w+")) == NULL ) {
		printf("can't open output file\n");
//		return -1;
	}

	/* Get number of test case */
	while ((EOF != (CurChar = fgetc(infile))) && 
		   ('\n' != CurChar)) {
		NumOfGame = NumOfGame * 10 + (CurChar - '0');
 	}
 	printf("NumOfCase : %d\n", NumOfGame);
	
	for (i=0; i<NumOfGame; i++) {
		int Tmp[2];
		int Ret = GetVals(infile, Tmp, 2);
		int MoteStart = Tmp[0];
		int MoteSize = Tmp[1];
		int Motes[MoteSize];
		int Ans = 0;
		int CurMote = MoteStart;
		int CurCnt = 0;
		Ret = GetVals(infile, Motes, MoteSize);

		if (1==MoteStart) {
			fprintf(outfile, "Case #%d: %d\n", i+1, Tmp[1]);
			continue;
		}
		
		Sort(Motes, MoteSize);
//		printf("case %d \n", i+1);
		for (j=0; j<MoteSize; j++) {
			if (CurMote > Motes[j]) {
				CurMote += Motes[j];
			} else {
				// rest num = MoteSize - j
				CurCnt = 0;
				while (CurMote <= Motes[j]) {
					CurMote = CurMote*2 - 1;
					CurCnt++;
				}
				CurMote += Motes[j];

				if (CurCnt >= (MoteSize - j)) {
//					printf("CurCnt = %d, is too big [%d]\n", CurCnt, MoteSize - j);
					Ans += (MoteSize - j);
					break;
				} else {
//					printf("CurCnt = %d, CurMote = %d\n", CurCnt, CurMote);
					Ans += CurCnt;
				}
			}
		}
		
//		system("pause");
		
		fprintf(outfile, "Case #%d: %d\n", i+1, Ans);
	}

    fclose(infile);
    fclose(outfile);
    
	return 0;
}
