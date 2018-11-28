#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define all(c) c.begin(), c.end() 
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
//#define tr(container, it) \
#define gcd __gcd
#define oo  (int)13e7

int main()
{
	int T;
	cin >> T;
	for ( int tt = 0 ; tt < T; tt++ )
	{
		int N,M;
		cin >> N >> M;
		int matrix[200][200];
		for ( int i = 0 ; i < N; i++ )
		{
			for ( int j = 0 ; j < M; j++ )
			{
				cin >> matrix[i][j];
			}
		}
		cout << "Case #"<<(tt+1)<<": ";
		//int nLoops = 10;
		bool usedRows[500], usedCol[500];
		REP(i,N) usedRows[i] = false;
		REP(j,M) usedCol[j] = false;
		while (true )
		{
			//if ( nLoops == 0 ) break;
			//nLoops--;
		        //cout << "start " << nLoops<<endl;	
			//cout << " entering while! ";
			bool yes = true;
			// if all are -1 we are done
			for ( int i = 0 ; i < N && yes; i++ ) if ( !usedRows[i] ) yes = false; 
			for ( int j = 0 ; j < M && yes; j++ ) if ( !usedCol[j] ) yes = false;
			if ( yes )
			{
				cout << "YES"<<endl;
				break;
			}	
			//search for a column
			// find the minimum column
			int minVal = 100000;
			for ( int i = 0 ;i < N; i++ )
			{
				for ( int j = 0 ; j < M; j++ )
				{
				//	cout << matrix[i][j] << " " ;
					if ( matrix[i][j] != -1 )
						minVal = min(matrix[i][j],minVal);
				}
//				cout << endl;
			}
			bool filled = false;
			// check if there is a row with only this minimum numbers;
			for ( int i = 0 ; i < N; i++ )
			{
				if ( usedRows[i] ) continue;
				bool useThisRow = true;
				for ( int j = 0 ; j < M; j++ )
				{
					if ( matrix[i][j] != -1 && matrix[i][j] != minVal )
					{
						useThisRow = false;
					}
				}
				if ( useThisRow )
				{
					REP(j,M)
					{
						matrix[i][j] = -1;
					}
					filled = true;
					usedRows[i] = true;
					break;
				}
			}
			if ( filled ) continue;
			REP(j,M)
			{
				bool useThisCol = true;
				if ( usedCol[j] ) continue;
				REP(i,N)
				{
					if ( matrix[i][j] != -1 && matrix[i][j] != minVal )
					{
						useThisCol = false;
					}
				}
				if ( useThisCol )
				{
					REP(i,N)
					{
						matrix[i][j] = -1;
					}
					usedCol[j] = true;
					filled = true;
					break;
				}
			}
			if ( !filled ){
				cout << "NO" <<endl;
				 break;
			}
		}
	}
}
