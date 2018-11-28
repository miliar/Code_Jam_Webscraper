#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <bitset>
#include <cstdlib>
#include <ctype.h>
#include <list>
#include <stack>
#include <deque>
#include <cmath>
#include <string>
#include <string.h>
#include <fstream>
using namespace std;
#define rep(i,n) for(int i = 0;  i < n ; ++i)
#define REP(i,a,b) for(int i = a ; i <= b ; ++i)
#define s(n) scanf("%d",&n)
#define rev(i,n) for(int i = n ; i >= 0 ; --i)
#define REV(i,a,b) for(int i = a ; i >= b ; --i)
#define maX(a,b) (((a)>(b))?(a):(b))
#define miN(a,b) (((a)<(b))?(a):(b))
#define sc(n) scanf("%c",&n)
#define swap(a,b) {int anujyadav = a ; a = b ; b = anujyadav ; }
		
int main()
{
	ifstream fin("as.in");
	ofstream fout("asmall.out") ;
	int t , q1 , q2 , counter = 0 , ans , A[4][4] , B[4][4]   ; 
	fin >> t ;
	for(int tc = 1 ;  tc <= t ; ++tc)
	{
		counter = 0  ;
		fin >> q1 ;
		for(int i = 0 ; i < 4 ; ++i)
		{
			for(int j = 0 ; j < 4 ; ++j)
			{
				fin >> A[i][j] ;
			}
		}
		fin >> q2 ;
		for(int i = 0 ; i < 4 ; ++i)
		{
			for(int j = 0 ; j < 4 ; ++j)
			{
				fin >> B[i][j] ;
			}
		}
		for(int i = 0 ; i < 4 ; ++i)
		{
			for(int j = 0 ; j < 4 ; ++j)
			{
				if(B[q2-1][j] == A[q1-1][i])
				{
					counter++ ;
					ans = B[q2-1][j] ;
				}
			}
		}
		if(counter == 1 )
			fout<<"Case #"<<tc<<": "<<ans<<"\n" ;
		else if(counter == 0)
		{
			fout<<"Case #"<<tc<<": "<<"Volunteer cheated!"<<"\n" ;
		}
		else 
			fout<<"Case #"<<tc<<": "<<"Bad magician!"<<"\n" ;
	}
}
	




 
