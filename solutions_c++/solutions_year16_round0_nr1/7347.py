#include<bits/stdc++.h>
using namespace std;

int main()
{
	int T, j, m;
	cin>>T;
	
	for(j=1; j<=T; j++)
	{
		long long int ans, k, S;
		int N, flag=0;
		cin>>N;
		
		int count[10];
		
		for(m=0; m<10; m++)
		count[m]=0;
		
		if(N==0)
		cout<<"Case #"<<j<<": INSOMNIA";
		
		else
		{
			k=1;
			while(1)
			{
				S=N*k;
				
				while(S!=0)
				{
					if(count[S%10]==0)
					flag++;
					count[S%10]++;					
					S=S/10;
				}
				
				if(flag==10)
				break;
				k++;
			}
			ans=N*k;
			cout<<"Case #"<<j<<": "<<ans;
		}
		cout<<endl;
	}
	return 0;
}
