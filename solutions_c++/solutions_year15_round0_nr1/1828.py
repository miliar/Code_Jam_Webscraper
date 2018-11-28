#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;
int n;
string str;
void solve(){
	cin>>n>>str;
	int ans=0,sum=0;
	for(int i=0;i<=n;i++){
		if(sum<i){
			ans+= i - sum;
			sum+= i - sum;
		}
		sum+=(str[i]-'0');
	}
	printf("%d\n",ans);
}
int main(){
	freopen("a.big.in","r",stdin);
	freopen("a.big.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		printf("Case #%d: ",cas);
		solve();
	}
	return 0;
}
