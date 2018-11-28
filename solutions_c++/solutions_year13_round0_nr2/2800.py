#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>

using namespace std;


bool CheckColumn(vector< vector<int> >& vField, int nStartRow, int nStartCol )
{
	for( int i = nStartRow; i < vField.size(); i++ )
	{
		if( vField[nStartRow][nStartCol] != vField[i][nStartCol] )
		{
				return false;
		}
	}
	return true;
}

bool CheckRow(vector< vector<int> >& vField, int nStartRow, int nStartCol )
{
	int nCurCol = nStartCol;

	for( int i = nStartCol; i < vField[nStartRow].size(); i++ )
	{
		if( vField[nStartRow][nCurCol] > vField[nStartRow][i] )
		{
			if( !CheckColumn(vField, 0, i) )
				return false;
		}
		else if( vField[nStartRow][nCurCol] < vField[nStartRow][i] )
		{
			if( !CheckColumn(vField, 0, nCurCol) )
				return false;
			nCurCol = i;
		}

	}
	return true;
}


int main()
{
	ifstream in("B-small-attempt0.in");
    ofstream out("B-small-attempt0.out");

	//ifstream in("B-large.in");
    //ofstream out("B-large.out");

	int iTasks;
	in >> iTasks;

	for( int iCount = 1; iCount <= iTasks; iCount++ )
	{
		int N, M;
		in >> N >> M;
		vector< vector<int> > vField;
		for( int i = 0; i < N; i++ )
		{
			vField.push_back(vector<int>(M));
			for( int j = 0; j < M; j++ )
			{
				in >> vField[i][j];
			}
		}
		bool bAvailable = true;
		for( int i = 0; i < N && bAvailable; i++ )
		{
			bAvailable = CheckRow(vField, i, 0);
		}
		out << "Case #" << iCount << ": ";
		if( bAvailable )
			out << "YES" << endl;
		else
			out << "NO" << endl;
	}
	return 0;
}
