// =====================================================================================
//       Filename:  MagicTric.cpp
//    Description:  
//        Created:  04/12/2014 09:05:38 AM
//         Author:  BrOkEN@!
// =====================================================================================

#include<fstream>
#include<iostream>
#include<sstream>
#include<bitset>
#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#include<iterator>
#include<string>
#include<cassert>
#include<cctype>
#include<climits>
#include<cmath>
#include<cstddef>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>

using namespace std;

template< class T > inline T _maxOfThree(T a,T b,T c) {return max(max(a,b),c);}
template< class T > inline T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _square(T x) { return x * x; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > bool in_range(T x, T i, T y) { return x<=i && i<=y; }

#define FOR(i,a,b) for(typeof((a)) i=(a); i <= (b) ; ++i)
#define REV_FOR(i,a,b) for(typeof((a)) i=(a); i >= (b) ; --i)
#define FOREACH(it,x) for(typeof((x).begin()) it=(x).begin(); it != (x).end() ; ++it)
#define REV_FOREACH(it,x) for(typeof((x).rbegin()) it=(x).rbegin(); it != (x).rend() ; ++it)
#define SET(p, v) memset(p, v, sizeof(p))
#define CLR(p) SET(p,0)
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define ARRAY_SIZE(array) (sizeof(array) / sizeof((array)[0]))
#define __int64 long long

typedef pair<int,int> PI;
typedef vector<PI> VI;


const int MAX = 4;

int first[MAX],second[MAX];
int common;
int f,s;

int solve(int tc){
	sort(first,first+MAX);
	sort(second,second+MAX);
	
	int i=0,j=0,k=0;
	while(i!=MAX && j!=MAX){
		if(first[i]<second[j])	i++;
		else if(first[i]>second[j]) j++;
		else{
			common=first[i];
			k++,i++,j++;
		}
	}	

	if(k==0){
		printf("Case #%d: Volunteer cheated!\n",tc);
	}else if(k==1){
		printf("Case #%d: %d\n",tc,common);
	}else{
		printf("Case #%d: Bad magician!\n",tc);
	}

	return 0;
}


int main(){
	int T=0;
	scanf("%d",&T);
	int a,b,c,d;
	FOR(t,1,T){
		scanf("%d",&f);
		for(int i=0;i<MAX;i++){
			scanf("%d%d%d%d",&a,&b,&c,&d);
			if(i+1 == f){
				first[0]=a,first[1]=b,first[2]=c,first[3]=d;
			}
		}
		scanf("%d",&s);
		for(int i=0;i<MAX;i++){
			scanf("%d%d%d%d",&a,&b,&c,&d);
			if(i+1 == s){
				second[0]=a,second[1]=b,second[2]=c,second[3]=d;
			}
		}
		solve(t);
	}
	return 0;
}

