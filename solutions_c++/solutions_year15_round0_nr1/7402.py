#include <iostream>
using namespace std;
# include<cstdio>
int main() {
	int test,z=1;
	scanf("%d",&test);
	while(test--)
	{
		int nx,i,ans=0,cont=0;
		scanf("%d",&nx);
		string s;
		cin>>s;
		ans=s[0]-'0';
		for(i=1;i<=nx;i++){
			if(i>ans)
			{
				cont+=(i-ans);
				ans+=s[i]-'0'+i-ans;
			}
			else
			ans+=s[i]-'0';
		}
		printf("Case #%d: %d\n",z++,cont);
	}
	return 0;
}
