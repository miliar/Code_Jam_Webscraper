#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

//const char * fin = "A-large.in";
const char * fin = "D-small-attempt1.in";
//const char * fin = "q_D_small.test.txt";
//const char * fin = "q_A_large.test.txt";
//const char * fout = "q_A_small.test.out.txt";

typedef struct
{
	int X;
	int R;
	int C;
	void vClear() {X=R=C=0;}
} tstInput;

typedef struct 
{
	int iGab;
	void vClear() {iGab=0;}
	void vPrint() {cout << (iGab ? "GABRIEL" : "RICHARD");}
} tstOutput;

void vGet(istream & fs, tstInput & stIn)
{
	string s;
	int i,j,k;
	fs >> stIn.X >> stIn.R >> stIn.C;
}

void vSolve(tstInput & stIn, tstOutput & stOut)
{
	stOut.iGab = 10;

	if (stIn.X <= 1)
	{
		stOut.iGab = 1;
	}
	else if ((stIn.R * stIn.C) < (stIn.X) ||
	    (stIn.R * stIn.C) % (stIn.X))
	{
		stOut.iGab = 0;
	}
	else if (stIn.X == 2)
	{
		stOut.iGab = ((stIn.R*stIn.C)%2) == 0 ? 1 : 0;
		//cout << "2 ";
	}
	else if (stIn.X == 3)
	{
		stOut.iGab = (stIn.R < 2 || stIn.C < 2) ? 0 : 1;
		//cout << "3 ";
	}
	else if (stIn.X == 4)
	{
		stOut.iGab = (stIn.R * stIn.C <= 8) ? 0 : 1;
		//cout << "4 ";
	}


	if (stOut.iGab <10) return;

	cout << "LOLDUNNO";
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