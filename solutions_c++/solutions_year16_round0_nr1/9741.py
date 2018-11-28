#include<bits/stdc++.h>
using namespace std;
#define lli long long int
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out200.out","w",stdout);
	int T;
	cin>>T;
	for(int i=1;i<=T;++i)
	{
		lli N;
		cin>>N;
		if(N==0)
		{
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
		bool flag=true;
		int A[]={0,0,0,0,0,0,0,0,0,0};
		lli k=N;
		int ct=1;
		while(flag)
		{
			flag=false;
			while(k>0)
			{
				A[k%10]=1;
				k/=10;
			}
			for(int i=0;i<10;++i)
			{
				if(A[i]==0)
				{
					flag=true;
					break;
				}
			}
			if(flag)
				k=(++ct)*N;
			else
				k=ct*N;	
		}
		N=k;
		cout<<"Case #"<<i<<": "<<N<<endl;
	}
	return 0;
}


