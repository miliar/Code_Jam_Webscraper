#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <stdlib.h>
#include <deque>
#include <list>
using namespace std;
#define INF 0x3fffffff
#define FOR(i,a,b)for( int i=a;i<=b;i++ )
#define fin freopen("A-small-attempt0(4).in","rt",stdin)
#define fout freopen("out.out","wt",stdout)
#define mod 1000002013
int n , m ;
int o[1005],e[1005],p[1005];

map<int,int> Start , End ;
set<int> S , E ;
int ss[1005],s_num[1005],ee[1005],e_num[1005];
int Indexs , Indexe ;
int main(){
	fin;
	fout;
	int cas , casn = 1 ;
	scanf("%d",&cas);
	while(cas--){
		scanf("%d%d",&n,&m);
		Indexs = 0 ;
		Indexe = 0 ;
		Start.clear();
		End.clear();
		S.clear();
		E.clear();
		long long ans1 = 0 ;
		FOR(i,1,m){
			scanf("%d%d%d",&o[i],&e[i],&p[i]);
			Start[o[i]]+=p[i];
			End[e[i]]+=p[i];
			int k = abs( o[i] - e[i] );
			ans1 += p[i] * ( n + n - k + 1 ) * k / 2 ;
		}
		map<int,int>::iterator it ;

		for( it = Start.begin() ; it != Start.end() ; it++ ){
			
			S.insert(it->first);
		}
		for( it = End.begin() ; it!=End.end() ; it ++ ){
		
			E.insert(it->first);
		}
		long long ans = 0 ;
		set<int>::iterator it1 = S.end() , it2 , tmp ;
		--it1;
		while( true ){
			int num1 = Start[*it1] ;
			it2 = E.lower_bound( *it1 );
			int num2 = End[*it2] ;
			int Min = min( num1 , num2 );
			int k = abs( *it1 - *it2 );
			ans += Min * ( n + n - k + 1 ) * k / 2 ;
			num1 -= Min ;
			num2 -= Min ;
			if( num2 == 0 ) E.erase( it2 );
			else{
				End[*it2]-=Min ;
			}
			if( num1 == 0 ){
				S.erase(it1);
				if( S.size() == 0 )break;
				it1=S.end();
				it1--;
			}else{
				Start[*it1]-=Min ;
			}
		}
		printf("Case #%d: %lld\n",casn++,ans1 - ans);
	}
	return 0 ;
}
