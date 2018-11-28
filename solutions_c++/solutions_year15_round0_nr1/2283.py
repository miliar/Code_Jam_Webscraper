#include <cstdio>
#include <iostream>
using namespace std;
int T,n,a[10005];
int ch[10005];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-small.out","w",stdout);
	scanf("%d",&T);
	int ca=1;
	while(T--){
		scanf("%d",&n);
		for (int i=0;i<=n;i++)scanf(" %c",&ch[i]);
		for (int i=0;i<=n;i++)a[i]=(int)ch[i]-'0';
		int now=0;
		int ans=0;
		for (int i=0;i<=n;i++){
			if(now<i&&a[i]){
				ans+=(i-now);
				now=i;
			}
			now+=a[i];
			//cout<<now<<' '<<a[i]<<' '<<ans<<endl;
		}
		printf("Case #%d: %d\n",ca++,ans);
	}
}
