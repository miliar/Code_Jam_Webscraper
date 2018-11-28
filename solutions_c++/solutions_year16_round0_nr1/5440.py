#include <bits/stdc++.h>
#define ll long long int

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	int t,n,temp,val,m[10];
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>n;
		val=0;
		for(int j=0;j<10;j++)
			m[j]=0;
		for(int j=1;j<=100;j++)
		{
			temp=j*n;
			while(temp)
			{
				if(!m[temp%10])
					val++;
				m[temp%10]=1;
				temp/=10;
				if(val == 10)
				{
					cout<<"Case #"<<i<<": "<<j*n<<"\n";
					break;
				}
			}
			if(val == 10)
				break;
		}
		if(val != 10)
			cout<<"Case #"<<i<<": INSOMNIA\n";
	}
	return 0;
}