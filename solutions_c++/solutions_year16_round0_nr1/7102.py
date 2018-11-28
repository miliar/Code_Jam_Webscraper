#include <bits/stdc++.h>
using namespace std;
#define ll long long 

void mark(int A[],ll ans)
{
	while(ans)
	{
		A[ans%10]=1;
		ans/=10;
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	int t;
	cin >> t;
	
	for(int i=1;i<=t;i++)
	{
		ll n;
		cin >> n;
		
		if(n==0)
		{
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		else
		{
			int A[10];
			for(int j=0;j<10;j++)
				A[j]=0;
			
			ll ans=n,count=1;
			
			while(true)
			{
				mark(A,ans);
				
				int sum=0;
				for(int j=0;j<10;j++)
				{
					sum+=A[j];
				}
				if(sum==10)
					break;
				
				count++;
				ans = n*count;
			}
			
			cout << "Case #" << i << ": " << ans << endl;
		}
	}
}
