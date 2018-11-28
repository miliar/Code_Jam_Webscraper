#include <iostream>
#include <iomanip>
#include <climits>
#include <stack>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <cassert>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define vi vector<int>
#define fs first
#define sec second

#define maxn 200

using namespace std;
typedef long long ll;

const ll MOD = 1000000007LL;

//double memo[maxn+2][maxn+2][maxn+2];
double p[maxn+2];
double s[maxn+2];

/*double dp(int n, int k, int v){
	if(k==0 && v==0)return 1.0;
	if(v<0 || k<0)return 0.0;
	if(k<v)return 0.0;
	if(n+1<k)return 0.0;
	if(n<0)return 0.0;
	if(memo[n][k][v]>=0.0)return memo[n][k][v];
	memo[n][k][v]=max(p[n]*dp(n-1,k-1,v-1)+(1.0-p[n])*dp(n-1,k-1,v),dp(n-1,k,v));
	cout << "n: "<<n<<" k: "<<k <<" v: "<<v<<" res: "<<memo[n][k][v]<<endl;
	return memo[n][k][v];
}*/

double memo[maxn+2][maxn+2];

double dp(int i, int j){
	if(i+1<j)return 0.0;
	if(i==-1 && j==0)return 1.0;
	if(i<0||j<0)return 0;
	if(memo[i][j]>=0.0)return memo[i][j];
	memo[i][j]=s[i]*dp(i-1,j-1)+(1-s[i])*dp(i-1,j);
	return memo[i][j];
}

void solve(int prim){
	int k,n;
	scanf("%d%d",&n,&k);
	FOR(i,n)scanf("%lf",p+i);
	double bst=0.0;
	FOR(mask,(1<<n)){
		int st=0;
		if(__builtin_popcount(mask)!=k)continue;
		FOR(i,n)FOR(j,n)memo[i][j]=-1;
		FOR(j,n){
			if(!(mask&(1<<j)))continue;
			s[st++]=p[j];
		}
		double tr=dp(k-1,k/2);
		if(tr>bst)bst=tr;
	}
	//FOR(i,maxn)FOR(j,maxn)FOR(k,maxn)memo[i][j][k]=-1;
	printf("Case #%d: %.12lf\n",prim, bst);
}

int main(){
	int n;
	scanf("%d",&n);
	FORR(i,1,n+1)solve(i);
	return 0;
}
