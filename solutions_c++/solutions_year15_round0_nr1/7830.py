#include<iostream>
using namespace std;
int main()
{
	int t,i,j,smax,p;
	long long int total,ans,temp;
	char s[10001];
	cin>>t;p=1;
	while(t)
	{
		ans=0;total=0;
		cin>>smax;
		cin>>s;

		for(i=0;i<=smax;i++)
		{
			j=s[i]-'0';
			if(total>=i)
			{
				total=total+j;
			}
			else if(total < i)
			{
				ans=ans+i-total;
				temp=i-total;
				total=total+temp+j;
			}
		}
		cout<<"Case #"<<p<<": "<<ans<<endl;
		t--;p++;
	}
	return 0;
}
