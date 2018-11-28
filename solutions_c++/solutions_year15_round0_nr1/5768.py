#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define mod 1000000007
char str[2000];
int ar[2000];
int main()
{
	int t,n,i;
	scanf("%d",&t);
	int x=1;
	while(t--)
	{
		scanf("%d",&n);
		char ch=getchar();
		scanf("%s",str);
		//printf("%s\n",str);
		for(i=0;str[i];i++)
		{
			ar[i]=str[i]-'0';
		}
		int psum=0;
		int ans=0;
		for(i=0;i<=n;i++)
		{
			if(psum<i)
			{
				ans+=i-psum;
				psum=i;
			}
			
				psum+=ar[i];
		}
		cout<<"Case #"<<x<<": "<<ans<<"\n";
		x++;
	}
	return 0;
}