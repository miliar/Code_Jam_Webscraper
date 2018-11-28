#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define FORI(i,n) REP(i,1,n)
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define SORT(X) sort(X.begin(),X.end())
#define fi first
#define se second

vector<int> A,B;
int T;

void test(){
	A.clear();
	B.clear();
	int a;
	scanf("%d",&a);
	FOR(i,4)
		FOR(j,4){
			int x;
			scanf("%d",&x);
			if(i+1 == a) A.pb(x);
		}
	scanf("%d",&a);
	FOR(i,4)
		FOR(j,4){
			int x;
			scanf("%d",&x);
			if(i+1 == a) FOR(k,SZ(A)) if(x == A[k]) B.pb(x);
		}
	printf("Case #%d: ",++T);
	if(SZ(B) == 1) printf("%d\n",B[0]);
	if(SZ(B) >  1) printf("Bad magician!\n");
	if(SZ(B) == 0) printf("Volunteer cheated!\n");
}

int main () {
	int t;
	scanf("%d",&t);
	while(t--) test();
}

