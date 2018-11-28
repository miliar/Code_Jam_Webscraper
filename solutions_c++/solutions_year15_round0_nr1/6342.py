#include <iostream>
#include <string>
using namespace std;
int main()
{
	int t,n,i,sum,count,j;
	cin>>t;
	j=1;
	while(j<=t)
	{
		count=0;
		cin>>n;
		char a[n+1];
		for(i=0;i<=n;i++)
			cin>>a[i];
		sum=a[0]-'0';
		for(i=1;i<=n;i++)
		{
			if((sum>=i )||(a[i]=='0'))
			{
				sum+=(a[i]-'0');
			}
			else
			{ 
				while(sum<i){
				sum+=1;
				count++;
				}
			sum+=(a[i]-'0');	
			}
		}	

	cout<<"Case #"<<j<<": "<<count<<"\n";
	j++;	
	}
}