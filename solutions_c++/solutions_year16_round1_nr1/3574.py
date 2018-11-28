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
	char str[1024];
	rep(n,N){
		cin >> str;
		char gen[4096];
		char *s = &gen[4096/2];
		char *e = &gen[4096/2-1];
		char *c = str;
		
		for(; *c ; c++){
			if( *s <= *c ){
				s--;
				*s = *c;
			}else{
				e++;
				*e = *c;
			}
			/*
			*(e+1) = 0;
			printf("%s\n",s);
			*/
		}
		*(e+1) = 0;
		
		printf("Case #%d: %s\n",n+1,s);
	}
	return 0;
}
