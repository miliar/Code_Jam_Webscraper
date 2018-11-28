//{{{
#define DEF
#ifdef DEF
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <stack>
#include <vector>
#include <list>
#include <map>
#include <cctype>
#include <queue>
#include <cstring>
#include <cmath>
#include <set>
#include <deque>


//-----------------------------------------------------


using namespace std;
typedef unsigned int uint;
typedef long long int llint;
typedef unsigned long long int ullint;

typedef pair<int,int> Pii;
typedef pair<llint,llint> Pll;

#define mrepp(i,n,x)  for(int i = n-1; i >= x; i--)
#define mrep(i,n) mrepp(i,n,0)
#define repp(i,x,n)  for(int i = x; i < n; i++)
#define rep(i,n) repp(i,0,n)
#define pb        push_back
#define all(vec)  (vec).begin(),(vec).end()
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
//#define reach(i,c) for(__typeof((c).rbegin()) i=(c).rbegin();i!=(c).rend();i++)
#define fst         first
#define scd         second

#define sz(v)     ((llint)(v).size())
//#define bit(n)    (1ll<<(li)(n))
//#define mkP        make_pair

//-----------------------------------------------------
#endif
//}}}


#define MAXNUM 10000000
int main(){
	int N;
	cin >> N;
	rep(i,N){
		int x;
		cin >> x;
		//x = i;
		
		char cnt[10];rep(k,10)cnt[k]=0;
		int j;
		llint num;
		char unsolve = 0;
		for(j=1;j<MAXNUM;j++){
			num =  x * ( j ) ;
			
			llint temp = num;
			for(;;){
				cnt[ temp%10 ] = 1;
				if( temp < 10 ) break;
				temp /= 10;
			}
			/*
			fprintf(stderr,"%10d : ",num);
			rep(x,10) fprintf(stderr,"%d : ",cnt[x]);
			fprintf(stderr,"\n");
			*/
			
			char break_flag = 1;
			rep(k,10){
				if( !cnt[k] ){
					break_flag = 0;
				}
			}
			if( break_flag ) break;
			
			if( MAXNUM == j + 1 ){
				unsolve = 1;
			}
		}
		
		if( unsolve ){
			//fprintf(stderr,"un-soloved : %d\n",x);
			printf("Case #%d: INSOMNIA\n",i+1);
		}else{
			printf("Case #%d: %lld\n",i+1,num);
		}
	}
	return 0;
}
