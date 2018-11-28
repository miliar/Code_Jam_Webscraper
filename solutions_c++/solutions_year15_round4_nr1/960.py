
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <ctime>
typedef long long ll;
#define clr(x,a) memset(x,a,sizeof(x))
#define sz(x) (int)x.size()
#define see(x) cerr<<#x<<" "<<x<<endl
#define se(x) cerr<<" "<<x 
#define pb push_back
#define mp make_pair
#define rep(i,l,r) for (long long i=l;i<=r;i++)
using namespace std;
double f[101000];
int n,w;
double p,ans;
int main(){
	int T;cin>>T;
	for (int cas=1;cas<=T;cas++){
		scanf("%d %lf %d",&n,&p,&w);
		double k=p/(1-p);
		f[0]=0;
		for (int i=0;i<n+w;i++){
			f[i+1]=(f[i]+1)*(1-p)+(f[i]+1)*k*(1-p);
		}
		cout<<k<<endl;
		cout<<f[1]<<endl;
		ans=f[n]+w;
		for (int i=1;i<=n;i++){
			ans=min(ans,n*f[w]+ (n)%i*f[(n)/i+1]+ (i-(n)%i)*f[(n)/i]);
		}
		printf("Cass #%d: %.6lf\n",cas,ans);
	}
	return 0;
}

