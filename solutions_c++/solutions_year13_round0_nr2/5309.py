// ProbA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "fstream"
#include "math.h"

#define INFILE "B-large.in"
#define OUTFILE "B-large.out"

using namespace std;

int n,m;
int mat[101][101];

bool canEscapeX(int i, int j)
{
	for (int k = 0; k<m; k++)
		if (mat[i][k]>mat[i][j])
			return false;
	return true;
}

bool canEscapeY(int i, int j)
{
	for (int k = 0; k<n; k++)
		if (mat[k][j]>mat[i][j])
			return false;
	return true;
}

bool canEscape(int i, int j)
{
	if (canEscapeX(i,j))
		return true;
	if (canEscapeY(i,j))
		return true;
	return false;
}

int _tmain(int argc, _TCHAR* argv[])
{
	char str[1000];	
	ifstream infile(INFILE);
	ofstream outfile(OUTFILE);
	
	int t;
	infile>>t;
	int count;
	//infile.getline(str,1000);
	for (int i=0; i<t; i++)
	{
		infile>>n>>m;
		for (int j=0; j<n; j++)
			for (int k = 0; k<m; k++)
				infile>>mat[j][k];

		outfile<<"Case #"<<i+1<<": ";
		bool isYes = true;
		for (int j = 0; j<n; j++)
		{
			for (int k = 0; k<m; k++)
				if (!canEscape(j,k))
				{
					isYes = false;
					break;
				}
			if (!isYes)
				break;
		}
		if (isYes)
			outfile<<"YES\n";
		else
			outfile<<"NO\n";
	}

	infile.close();
	outfile.close();
	return 0;
}

