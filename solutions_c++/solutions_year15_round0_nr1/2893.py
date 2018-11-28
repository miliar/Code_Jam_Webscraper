#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("F:\\TestFiles\\A-large.in","r",stdin);
	freopen("F:\\TestFiles\\A-large.out","w",stdout);
	
	int t; scanf("%d",&t);
	int testcase=1;
	while(t--){
		
		int n;scanf("%d",&n);
		char a[1005];scanf("%s",a);
		int len=strlen(a);
		
		int ans=0,sum=0;
		for (int i=0;i<len;i++){
			if (i-sum>=0){
				ans+=(i-sum);
				sum+=(a[i]-'0'+i-sum);
			}
			else
			{
				sum+=(a[i]-'0');
			}
		}
		
		printf("Case #%d: %d\n",testcase++,ans);
	}
	
	return 0;
}