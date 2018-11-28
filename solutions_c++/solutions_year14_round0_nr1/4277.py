#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <algorithm>
#include <iostream>
#include <assert.h>

using namespace std;

#define SET(v,i) memset(v,i,sizeof(v));
#define FOR(i,n,k) for(int i=n;i<k;++i)
#define WHILE(i,n) while(i<n)
#define RI(i) scanf("%d",&i);
#define RS(i) scanf("%s",i);
#define RF(i) scanf("%lf",&i);
#define RL(i) scanf("%lld",&i);
#define OPEN(s) freopen(s,"r",stdin);
#define CLOSE(s) freopen(s,"w",stdout);

const int INF=0x3F3F3F3F;
const int MAXN=100001;
typedef long long int i64;
typedef pair<int,int> pii;
typedef pair<string,int> psi;

set<int> same;

int main(){
	#ifdef DM1_MACHINE
		OPEN("FILE.in");
		CLOSE("FILEa.out");
	#endif
	int t; RI(t);
	FOR(ic,1,t+1){
		same.clear();
		int n; RI(n);
		int num;
		FOR(i,0,4){
			FOR(j,0,4){
				RI(num);
				if(i==n-1){
					same.insert(num);
				}
			}
		}
		RI(n);
		int find_cnt = 0;
		int first_find = -1;
		FOR(i,0,4){
			FOR(j,0,4){
				RI(num);
				if(i==n-1){
					if(same.find(num)!=same.end()){
						first_find = num;
						find_cnt++;
					}
				}
			}
		}
		printf("Case #%d: ",ic);
		if(find_cnt==1) printf("%d\n",first_find);
		else if(find_cnt<=0) printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
	}
	return 0;
}


////////////////////////////////////////////
/////////////Code by David Moran////////////
/////////////////////////////P=NP///////////
