#include <iostream>
#include<cstring>
using namespace std;

int main() {
	int t,n,p,i,f,ans,ca;
	cin>>t;
	while(t--)
	{
		ca=ca+1;
		char str[10000];
		scanf("%s",str);
		n=strlen(str);
		p=0;
		int k=0;
		f=0;
		for(i=0;i<n;i++)
		{
			if(str[i]=='+' && str[i+1]=='-')
			{
				f=f+1;
			}
		}
		if(str[0]=='-')
		{
			f=f+1;
			ans=(2*f)-1;
		//cout<<ans<<endl;
		printf("Case #%d: %d\n",ca,ans);
		}
		else
		{
			ans=(2*f);
			//cout<<ans<<endl;
			printf("Case #%d: %d\n",ca,ans);
		}
	}
	return 0;
}