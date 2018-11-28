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
#include <iomanip>
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
#define INF 1000000000
int main()
{
	ifstream fin("bs.in");
	ofstream fout("bsmall.out") ;
	int t ; 
	double z , C , F , X , time , min , sum ; 
	fin >> t ;
	for(int tc = 1 ; tc <= t ; ++tc)
	{
		min = INF ;
		fin >> C >> F >> X ;
		for(int z = 0 ; z <= 2001 ; ++z)
		{
			time = X/(2 + z*F) ;
			sum = 0 ;
			for(int i = 0 ; i < z ; ++i)
			{
				sum += 1/(2 + i*F) ;
			}
			if(z != 0)
				sum *= C ;
			time += sum ;
			if(time < min)
				min = time ;
		}
		
		fout <<"Case #"<<tc<<": "<<setprecision(7)<<fixed<<min<<"\n" ;
	}
	return 0 ;   
			
	
	
}
	




 
