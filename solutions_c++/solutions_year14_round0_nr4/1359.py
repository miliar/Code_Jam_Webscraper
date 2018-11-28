#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#define X first
#define Y second
#define fo(i,n) for(int i=0;i<n;i++)
#define fr(i,n) for(int i=1;i<=n;i++)
#define pb push_back

using namespace std;

typedef long long ll;

const int mod=(int)1e9+7;
int T,n,cas;
double a[1010],b[1010];
int main(){
	//freopen("dl.in","r",stdin);
	//freopen("dl.out","w",stdout);
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		fr(i,n) scanf("%lf",&a[i]);
		fr(i,n) scanf("%lf",&b[i]);
		sort(a+1,a+n+1);
		sort(b+1,b+n+1);
		printf("Case #%d:",++cas);
		for(int i=1;i<=n;i++){
			bool flag=true;
			for(int j=i;j<=n;j++)
				if(a[j]<b[j-i+1])
					flag=false;
			if(flag){
				printf(" %d",n-i+1);
				break;
			}
			if(i==n) printf(" 0");
		}
		int ans=0;
		int j=n;
		for(int i=n;i>=1;i--)
			if(b[j]>a[i]) j--;
			else ans++;
		printf(" %d\n",ans);
	}
	return 0;
}

