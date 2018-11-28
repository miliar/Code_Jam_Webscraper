#include <bits/stdc++.h>

using namespace std;


int main()
{
	int T;
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	for(int ii=1;ii<=T;ii++)
	{
		int N;
		cin>>N;
		map<int,int> M;
		long long int ans=-1;
		for(int i=1;i<=100000;i++)
		{
			long long int temp = i*N;
			while(temp>0)
			{
				M[temp%10]++;
				temp=temp/10;
			}
			int flag=1;
			for(int j=0;j<10;j++)
			{
				if(M[j]==0)
				{
					flag=0;
					break;
				}
			}
			if(flag)
			{
				ans = i*N;
				break;
			}
		}
		if(ans==-1)
		{
			cout<<"Case #"<<(ii)<<": INSOMNIA\n";
		}
		else
		{
			cout<<"Case #"<<(ii)<<": "<<ans<<"\n";
		}
	}

	return 0;
}