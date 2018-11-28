#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

const char * fin = "A-small-attempt0.in";
//const char * fout = "q_A_small.test.out.txt";

typedef struct
{
	int iMax;
	int aiPerson[1000];
	void vClear() {iMax=0;int i;for(i=0;i<1000;++i)aiPerson[i]=0;}
} tstInput;

typedef struct 
{
	int iAns;
	void vClear() {iAns=0;}
	void vPrint() {cout << iAns;}
} tstOutput;

void vGet(istream & fs, tstInput & stIn)
{
	string s;
	int i,j,k;
	fs >> stIn.iMax;
	fs >> s;
	for (j=0; j<=stIn.iMax; ++j)
	{
		stIn.aiPerson[j] = s[j]-'0'; 
		//cout << stIn.aiPerson[j];
	}
}

void vSolve(tstInput & stIn, tstOutput & stOut)
{
	int iStanding=0;
	int iAdd=0;
	int i=0,j,k;

	while (i<=stIn.iMax)
	{
		
		if (iStanding < i)
		{
			j = i - iStanding;
			iAdd += j;
			iStanding += j;
		}
		iStanding += stIn.aiPerson[i];
		++i;
		//cout << iStanding << endl;
	}
	stOut.iAns = iAdd;
}

void vPrint(int iId, tstOutput & stOut)
{
	cout << "Case #" << iId << ": ";
	stOut.vPrint();
	cout << endl;
}

int main()
{
	int i,j,k,n;

	tstInput stIn; tstOutput stOut;
	string s;
	fstream fs;

	fs.open(fin, ios::in);
	fs >> n;

	for (i=1; i<=n; ++i)
	{
		stIn.vClear();
		stOut.vClear();
		vGet(fs, stIn);
		vSolve(stIn, stOut);
		vPrint(i, stOut);
	}

	fs.close();


	return 0;
}