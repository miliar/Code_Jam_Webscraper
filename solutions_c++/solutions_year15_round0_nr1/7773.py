#include<iostream>
#include<stdlib.h>
#include<stdio.h>

using namespace std;

int main(void)
{
	FILE *f1,*f2;
	f1=freopen("A-large.in","r",stdin);
	f2=freopen("So.out","w",stdout);
	long long int t,i,ans,smax,j,sum=0;
	cin>>t;
	j=t;
	while(t--)
	{
		sum=ans=0;
		cin>>smax;
		char s[smax+1];
		cin>>s;
		sum=(s[0]-48);
		
		for(i=1;s[i]!='\0';i++)
		{
			if(s[i]!='0')
			{
				if(sum>=i)
					sum+=(s[i]-48);
				else
				{
					ans+=i-sum;
					sum+=(i-sum)+(s[i]-48);
				}
			}
		}
		cout<<"Case #"<<j-t<<": "<<ans<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
