#include <stdio.h>
#include <vector>

//FILE * in = fopen("Input.txt" , "r");
//FILE * out = fopen("Output.txt" , "w");

FILE * in = fopen("B-large.in" , "r");
FILE * out = fopen("B-large.out" , "w");

int T;
int D;

std::vector<int> vecP;
int nCnt;
int nMin;
void Input()
{
	int p;
	vecP.clear();
	fscanf(in, "%d", &D);

	for(int i=0; i<D; i++)
	{
		fscanf(in, "%d", &p);
		vecP.push_back(p);
	}
}

void Process()
{
	nCnt = 0;
	int nMax = 0;
	int nMax2 = 0;
	
	for(int i=0; i<vecP.size(); i++)
	{
		if (nMax < vecP.at(i))
		{
			nMax = vecP.at(i);
		}
	}
	nMin = nMax;

	for(int i=1; i<nMax; i++)
	{
		nCnt = 0;
		for(int j=0; j<vecP.size(); j++)
		{
			if (vecP.at(j)>i)
			{
				nCnt += (vecP.at(j)/i)-1;
				if (vecP.at(j)%i)
					nCnt++;
			}
		}
		if (nCnt+i<nMin)
			nMin = nCnt+i;
	}
}

void Output()
{
	fprintf(out, "Case #%d: %d\n", T, nMin);
}

int main()
{
	int nNumOfCase;

	fscanf(in, "%d", &nNumOfCase);	

	for(T = 1; T<=nNumOfCase; T++)
	{
		Input();
		Process();
		Output();
	}
	return 0;
}
