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
#define N 6250010
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
 
int main()
{
    FREOPEN("input.txt","output.txt");
	int test;
	double X,F,C,ans,cur,time;
	scanf("%d",&test);
	rep(t,test)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		cur=2.0;
		ans=X / cur;
		time=0;
		rep(i,10000000)
		{
			time+=C / cur;
			cur+=F;
			ans=min(ans,time + X / cur);
		}
		printf("Case #%d: %.9lf\n",t+1,ans);
	}
	return 0;   
} 