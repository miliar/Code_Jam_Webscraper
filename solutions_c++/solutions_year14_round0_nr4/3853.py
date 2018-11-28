#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <sstream>

using namespace std;

#define REP(i,a,b) 	for(int i=a;i<(int)b;i++)
#define FOR(it,A)	for(typeof A.begin() it=A.begin();it!=A.end();it++)
#define all(x) 		(x).begin(),(x).end()
#define pb 			push_back
#define clr(x,y)	memset(x,y,sizeof x)
#define oo 			(1<<30)
#define inf 		(1LL<<40)
#define bit(x)		__builtin_popcount(x)
#define mp			make_pair
#define fst			first
#define snd			second
#define maxN		100005
#define mod			1000000007

typedef long long     ll;
typedef vector<int>   vi;
typedef pair<int,int> pii;
typedef long double   ld;


int main(){
	
	
	int casos,n,W=0,DW=0;
	scanf("%d",&casos);
	REP(caso,1,casos+1){
		W = DW = 0;
		scanf("%d",&n);
		set<int> AA,A,B,BB;
		REP(i,0,n){
			double a;
			scanf("%lf",&a);
			int aa = a*100000 + 0.5;
			A.insert(aa);
			AA.insert(aa);
		}
		REP(i,0,n){
			double b;
			scanf("%lf",&b);
			int bb = b*100000 + 0.5;
			B.insert(bb);
			BB.insert(bb);
		}
		FOR(it,AA){
			set<int>::iterator it2 = BB.upper_bound(*it);
			if(it2!=BB.end()) BB.erase(it2);
			else W++;
		}	
		for(typeof B.rbegin() it=B.rbegin();it!=B.rend();it++){
			set<int>::iterator it2 = A.upper_bound(*it);
			if(it2!=A.end()){
				A.erase(it2);
				DW++;
			}
			else A.erase(A.begin());
		}
		printf("Case #%d: %d %d\n", caso, DW, W);
	}
	
    return 0;
}






