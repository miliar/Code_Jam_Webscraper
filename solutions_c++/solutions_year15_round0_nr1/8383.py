#include<bits/stdc++.h>
#define lli long long int
using namespace std;
int main(){
	int t,T;
	scanf("%d",&t);
	T=1;
	while(t--){
		int arr[1005];char s[1005];
		lli n,ans=0,sol=0;
		scanf("%lld %s",&n,s);
		arr[0]=s[0]-'0';
		for(int i=1;i<=n;i++){
			arr[i]=s[i]-'0';
			arr[i]+=arr[i-1];
			if(arr[i-1]<i){
				ans=(i-arr[i-1]);
				arr[i]+=ans;
				sol+=ans;
			}
		}
		printf("Case #%d: %lld\n",T++,sol);
	}
	return 0;
}

