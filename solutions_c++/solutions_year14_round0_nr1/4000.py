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
	
	int casos;
	scanf("%d",&casos);
	REP(caso,1,casos+1){
		int n;
		scanf("%d",&n);
		set<int> s;
		int num;
		REP(i,1,5){
			REP(j,1,5){
				scanf("%d",&num);
				if(i==n){
					s.insert(num);
				}	
			}
		}
		scanf("%d",&n);
		int card = -1;
		int found = 0;
		REP(i,1,5){
			REP(j,1,5){
				scanf("%d",&num);
				if(i==n){
					if(s.find(num)!=s.end()){
						found++;
						card = num;
					}
				}	
			}
		}
		if(found == 0) printf("Case #%d: Volunteer cheated!\n",caso);
		else if( found > 1) printf("Case #%d: Bad magician!\n",caso);
		else printf("Case #%d: %d\n",caso,card);
	}
	
    return 0;
}






