#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int t,cs=0;
char pk[1111];
int main(){
	scanf("%d",&t);
	while(t--){
		int mx;
		scanf("%d",&mx);
		scanf("%s",pk);
		int ct=0,ans=0;
		for(int i=0;i<=mx;++i){
			//printf("hv:%d nd:%d \n",ct,i);
			if(ct<i){
				ans+=i-ct;
				ct=i;
			}
			ct+=pk[i]-'0';
		}
		printf("Case #%d: %d\n",++cs,ans);
	}
	return 0;
}
