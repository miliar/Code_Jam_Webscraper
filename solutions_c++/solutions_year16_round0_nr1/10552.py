#include<bits/stdc++.h>

using namespace std;

bool arr[10];

int main()
{	
	ios::sync_with_stdio(false);
	int test,i;
	cin>>test;
	for(i=0;i<test;i++)
	{
		int n,now;
		for(int j=0;j<10;j++) arr[j]=false;
		cin>>n;
		now=n;
		if(!n)
		{
			cout<<"Case #"<<i+1<<": INSOMNIA\n";
			continue;
		}
		while(true)
		{	
			int j,k=n;
			while(k)
			{
				arr[k%10]=true;
				k/=10;
			}
			for(j=0;j<10;j++) if(!arr[j]) break;
			if(j==10) break;
			n+=now;
		}
		cout<<"Case #"<<i+1<<": "<<n<<"\n";
	}
	return 0;
}
