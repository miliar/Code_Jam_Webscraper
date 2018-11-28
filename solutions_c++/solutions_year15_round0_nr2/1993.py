#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
int a[8888];
int main()
{
    freopen("in.txt","r",stdin);
	freopen("out.out","w",stdout);
	int T;cin>>T;
	int cs=1;
	while(T--){
		int n;cin>>n;
		for(int i=0;i<n;i++){
			scanf("%d",&a[i]);
		}
		int ans=9999999;
		for(int i=1;i<=1000;i++){
			int dd=0;
			for(int j=0;j<n;j++){
				if(a[j]/i>=1){
					dd+=(a[j]/i)-1+(a[j]%i!=0);
				}
			}
			ans=min(dd+i,ans);
		}
		printf("Case #%d: %d\n",cs++,ans);
	}
	return 0;
}