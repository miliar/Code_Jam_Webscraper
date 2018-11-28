#include<bits/stdc++.h>
using namespace std;
#define lli long long int
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out2.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		lli n;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
		bool flag=true;
		int A[]={0,0,0,0,0,0,0,0,0,0};
		lli k=n;
		int count=1;
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
				k=(++count)*n;
			else
				k=count*n;	
		}
		n=k;
		cout<<"Case #"<<i<<": "<<n<<endl;
	}
	return 0;
}


