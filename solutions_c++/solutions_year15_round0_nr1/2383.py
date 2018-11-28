#include<bits/stdc++.h>
using namespace std;
int  main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t,smax,i,counter,sum,temp,j=0;
	char str[2000];
	cin>>t;
	while(t--)
	{
		j++;
		cin>>smax;
		cin>>str;
		sum=str[0]-'0';
		counter=0;
		for(i=1;i<=smax;i++)
		{
			temp=str[i]-'0';
			if(sum<i&&str[i]>'0')
			{
				counter+=(i-sum);
				sum+=(i-sum);
			}
			sum+=temp;
		}
		cout<<"Case #"<<j<<": "<<counter<<"\n";	
	}
	return 0;	
}
