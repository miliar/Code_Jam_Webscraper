# include <iostream>
# include <string>
# include <cstdio>
using namespace std;
int main()
{
	int t,s,ans,count,i,temp,j;
	string str;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		count=0;
		ans=0;
		scanf("%d",&s);
		cin>>str;
		for(i=0;i<=s;i++)
		{
			if(count>=i)
				count+=str[i]-48;
			else
			{
				temp=i-count;
				ans=ans+i-count;
				count=count+str[i]+temp-48;
			}
		}	
		printf("Case #%d: %d\n",j,ans);
	}
	return 0;
}
