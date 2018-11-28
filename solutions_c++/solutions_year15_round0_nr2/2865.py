/*********************************************************
  file name: B.cpp
  author : kereo
  create time:  2015年04月11日 星期六 11时04分21秒
*********************************************************/
#include<iostream>
#include<cstdio>
#include<cstring>
#include<queue>
#include<set>
#include<map>
#include<vector>
#include<stack>
#include<cmath>
#include<string>
#include<algorithm>
using namespace std;
typedef long long ll;
const int sigma_size=26;
const int N=1000+50;
const int MAXN=100000+50;
const int inf=0x3fffffff;
const double eps=1e-8;
const int mod=1000000000+7;
#define L(x) (x<<1)
#define R(x) (x<<1|1)
#define PII pair<int, int>
#define mk(x,y) make_pair((x),(y))
int n;
int a[N];
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,kase=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		int Max=0,ans=inf;
		for(int i=1;i<=n;i++){
			scanf("%d",&a[i]);
			Max=max(Max,a[i]);
		}
		int tmp;
		for(int i=1;i<=Max;i++){
			tmp=0;
			for(int j=1;j<=n;j++){
				tmp+=(a[j]+i-1)/i-1;
			}
			ans=min(ans,tmp+i);
		}
		printf("Case #%d: %d\n",++kase,ans);
	}
	return 0;
}
