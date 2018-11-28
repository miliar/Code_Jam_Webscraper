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

int main()
{
	
	int t  , N , war , d_war , flag = 0 , ptr , i , j , ptr1  ;
	ifstream fin("cs.in");
	ofstream fout("csmall.out") ;
	fin >> t ;
	REP(tc,1,t) 
	{
		fin >> N ;
		d_war = 0 ;
		war = 0 ;
		ptr = N - 1 ;
		ptr1 = 0 ;
		vector<double> naomi(N) ;
		vector<double> ken(N) ;
		vector<bool> mark(N) ;
		vector<bool> mark1(N) ;
		rep(i,N) 
			fin >> naomi[i] ;
		rep(i,N) 
			fin >> ken[i] ;
		sort(naomi.begin(),naomi.end()) ;
		sort(ken.begin(),ken.end()) ;
		for(int i = 0 ; i < N ; ++i)
		{
			for(j = 0 ; j < N  ; ++j)
			{
				if(!mark[j] && naomi[i] > ken[j])
				{
					mark[j] = true ;
					d_war++ ;
					break ;
				}
			}
			if(j == N){
				mark[ptr] = true ;
				ptr-- ;
			}
		}
		for(int i = 0 ; i < N ; ++i)
		{
			for(j = 0 ; j < N ; ++j)
			{
				if(!mark1[j] && ken[j] > naomi[i])
				{
					mark1[j] = true ;
					break ;
				}
			}
			if(j == N)
			{
				for(int k = 0 ; k < N ;  ++k)
				{
					if(!mark1[k])
						war++ ;
				}
				break ;
			}
		}
		fout << "Case #"<<tc<<": "<<d_war<< " " << war << "\n" ; 
	}
	return 0;
}
	




 
