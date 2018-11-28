#include <iostream>
#include <string>
#include <fstream>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <stack>
#include <iomanip>
#include <math.h>
#include <map>
using namespace std;

#define LOCAL
#ifdef LOCAL  
    ifstream fin("D:/B-large.in");  
    #define cin fin  
    ofstream fout("D:/output.txt");  
    #define cout fout   
#endif  

int ss[100][100];

int N, M;
void Input()
{
	cin >> N; cin >> M;
	
	for(int i=0; i<N; i++)
		for(int j=0; j<M; j++)
			cin >> ss[i][j];
}
bool pendi(int row, int col)
{
	bool leftHigh = false;
	bool rightHigh = false;
	bool topHigh = false;
	bool bottomHigh = false;
	for(int i=0; i<row; i++)
	{
		if(ss[i][col] > ss[row][col])
		{	topHigh = true; break;}
	}
	
	for(int i=row+1; i<N; i++)
	{
		if(ss[i][col] > ss[row][col])
		{	bottomHigh = true; break;}
	}
	
	for(int i=0; i<col; i++)
	{
		if(ss[row][i] > ss[row][col])
		{	leftHigh = true; break;}
	}
	
	for(int i=col+1; i<M; i++)
	{
		if(ss[row][i] > ss[row][col])
		{	rightHigh = true; break;}
	}
	
	return (leftHigh || rightHigh) && (topHigh || bottomHigh);
}
bool Solve()
{
	
	for(int i=0; i<N; i++)
		for(int j=0; j<M; j++)
		{
			if( pendi(i, j) )
				return false;// not possible
		}
	return true; // possible
}



void Print(int caseIndex, bool possible)
{
	cout << "Case #" << caseIndex+1 << ": ";
	if(possible)
		cout << "YES" << endl;
	else
		cout << "NO" << endl;
}

int main()
{
	int caseNum; 
	cin >> caseNum;
	
	for(int i=0; i<caseNum; i++)
	{
		Input();
		bool result = Solve();
		Print(i, result);
	}

#ifdef LOCAL     
    system("PAUSE");
#endif
    return 0;
}

