#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define AL(x) x.begin(),x.end()
#define pw(x) (1ull<<(x))
#define M 1000000007
using namespace std;
typedef pair<int,int> pt;
typedef vector<int> vt;

int g[2222][2222],w[2222],ans[2222],a[2222],b[2222],n,o[2222],gg,oo[2222][111];

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);	
	int T=0;
	cin >> T;
	for (int E=1;E<=T;E++){
		cin >> n;
		for (int i=0;i<n;i++)for (int j=0;j<n;j++)g[i][j]=0;
		for (int i=0;i<n;i++)cin >> a[i];
		for (int i=0;i<n;i++)cin >> b[i];
		for (int i=0;i<n;i++){
			for (int j=i+1;j<n;j++)if (b[j]>=b[i])g[j][i]=1;
			for (int j=i+1;j<n;j++)if (b[i]==b[j]+1){
				g[i][j]=1;
				break;
			}
			for (int j=0;j<i;j++)if (a[j]>=a[i])g[j][i]=1;
			for (int j=i-1;j>=0;j--)if (a[i]==a[j]+1){
				g[i][j]=1;
				break;
			}
		}
		gg=(n+31)/32;
		for (int i=0;i<n;i++)for (int j=0;j<gg;j++)oo[i][j]=0;
		for (int i=0;i<n;i++)oo[i][i/32]+=pw(i%32);
		for (int i=0;i<n;i++)w[i]=0,o[i]=0;

		for (int i=0;i<n;i++)for (int j=0;j<n;j++)if (g[i][j])w[j]++;
		for (int i=0;i<n;i++){
			int l=-1;
			for (int j=0;j<n;j++)if (w[j]==0&&o[j]==0)l=j;
			o[l]=1;
			for (int j=0;j<n;j++)if (g[l][j]){
				w[j]--;
				for (int k=0;k<gg;k++)oo[j][k]|=oo[l][k];
			}
		}
		for (int i=0;i<n;i++)w[i]=0,o[i]=0;
		for (int i=0;i<n;i++)for (int j=0;j<n;j++)if (g[i][j])w[i]++;
		for (int i=0;i<n;i++){
			int l=-1;
			for (int j=0;j<n;j++)if (w[j]==0&&o[j]==0){
				if (l==-1){
					l=j;
					continue;
				}
				int sw=0;
				for (int k=0;k<gg;k++)if (oo[l][k]!=oo[j][k]){
					for (int u=0;u<32;u++){
						if ((oo[l][k]&pw(u))>0&&(oo[j][k]&pw(u))==0)break;
						if ((oo[l][k]&pw(u))==0&&(oo[j][k]&pw(u))!=0){
							sw=1;
							break;
						}
					}
					break;
				}
				if (sw)l=j;
			}
			o[l]=1;
			ans[l]=i+1;
			for (int j=0;j<n;j++)if (g[j][l])w[j]--;
		}
		cout << "Case #" << E << ":";
		for (int i=0;i<n;i++)cout << " " << ans[i];
		puts("");

	}
	return 0;
}


