#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;
typedef long long LL;
const int N=210;
double p[N];
double q[N],f[N][N];
double ans = 0;
int n,m;
void check(){
	f[0][0] = 1;
	for(int i=1;i<=m;i++)
	for(int j=0;j<=m/2;j++)
	{
		f[i][j] = f[i-1][j] * (1-q[i]);
		if(j>=1) f[i][j] += f[i-1][j-1] * q[i];
	}
	ans = max(ans,f[m][m/2]);
}
int main() {
	freopen("bb.in","r",stdin);
	freopen("bb.out","w",stdout);
	int numcase;
	cin>>numcase;
	for(int ii=1;ii<=numcase;ii++){
		cin>>n>>m;
		for(int i=1;i<=n;i++)
			scanf("%lf",&p[i]);
		sort(p+1,p+n+1);
		ans = 0;
		for(int i=0;i<=m;i++){
			q[i]=p[i];
			int t= i;
			for(int j=1;i+j<=m;j++)
				q[++t] = p[n-j+1];
			check();
		}	
		printf("Case #%d: %.10f\n",ii,ans);
	}
	return 0;
}
