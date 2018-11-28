#include <bits/stdc++.h>

using namespace std;

int f(int x)
{
	vector <bool> b(10,false);
	int ctr=0;
	for(int i=0;i<=72;i++)
	{
		int y=x*i;
		while(y)
		{
			if(!b[y%10])
			{
				b[y%10]=true;
				ctr++;
			}
			y/=10;
		}
		if(ctr==10)
			return x*i;
	}
	return 0;
}

int main()
{
	int testCases,number;
	cin>>testCases;
	for(int index=0;index<testCases;index++)
	{
		cin>>number;
		int ans=f(number);
		if(ans==0)
			cout<<"Case #"<<index+1<<": INSOMNIA\n";
		else
			cout<<"Case #"<<index+1<<": "<<ans<<endl;
	}
	return 0;
}