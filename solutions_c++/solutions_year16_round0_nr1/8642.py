#include<bits/stdc++.h>
#define N 1000000007
#define maxs 300005
#define mins 1005
#define pf printf
#define sc scanf
#define ll long long
#define pb push_back
using namespace std;
int a[10];
int main()
{
	int t;
	sc("%d",&t);
	for(int l=1;l<=t;l++)
	{
		ll n,n1;
		cout<<"Case #"<<l<<": ";
		sc("%lld",&n);
		n1=n;
		if(n==0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		ll k;
		int i,fl1=0;
		int j=1;
		for(i=0;i<10;i++)
		a[i]=0;
		while(1)
		{
			k=n;
			while(k>0)
			{
				a[k%10]=1;
				k=k/10;
			}
			fl1=0;
			for(i=0;i<10;i++)
			{
				if(a[i]==0)
				{
					fl1=1;
					break;
				}
			}
			if(fl1==0)
			break;
			n=(j+1)*n1;
			j++;
		//	cout<<n<<endl;
		}
		if(fl1==0)
		printf("%lld\n",n);
	}
	return 0;
}
