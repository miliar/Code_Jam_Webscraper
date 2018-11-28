#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <memory.h>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#pragma comment(linker,"/STACK:16777216")
 
using namespace std;
 
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define MEM(a,b) memset((a),(b),sizeof(a))
#define N 100010
#define inf 1000000000
#define pi 2*acos(0.0)
#define eps 1e-9
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define sz(x) int((x).size())
#define mp(a,b) make_pair((a), (b))
#define FREOPEN(a,b) freopen(a,"r",stdin); freopen(b,"w",stdout);
 
typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;


vint v[N];
int a[N],b[N];
int dp[N][333]={0};

int main()
{
    FREOPEN("input.txt","output.txt");
	int a,b,k,test,ans;
	scanf("%d",&test);
	rep(t,test)
	{
		ans=0;
		scanf("%d%d%d",&a,&b,&k);
		FOR(i,0,a - 1)
			FOR(j,0,b - 1)
			if((i & j) < k)ans++;
		printf("Case #%d: %d\n",t+1,ans);
	}
	return 0;   
}