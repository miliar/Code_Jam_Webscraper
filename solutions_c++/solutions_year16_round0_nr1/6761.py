//----------shivam_wadhwa----------//
#include <bits/stdc++.h>
#define ll long long int
#define sc1(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d%d",&x,&y)
#define pint(c) printf("%d",c)
#define pll(c) printf("%lld",c)
#define ps() printf(" ")
#define pn() printf("\n")

#define vi vector<int>
#define vii vector<pair<int,int> >
#define mp make_pair
#define pb push_back
#define MAX 10000000
#define MOD 1000000007
int hash[10];
using namespace std;
int main()
{
	int t=1;
	sc1(t);
	int k=1;
	while(k<=t)
	{
		int n;
		sc1(n);
		for(int i=0;i<10;++i)
		{
			hash[i]=0;
		}
		int count=2;
		if(n==0)
		{
			cout<<"Case #"<<k<<": INSOMNIA\n";
			k++;
			continue;
		}
		int temp=n;
		while(1)
		{
			
			while(temp)
			{
				hash[temp%10]=1;
				temp/=10;
			}
			int i;
			for(i=0;i<10;++i)
			{
				if(hash[i]==0)
					break;
			}
			if(i<10)
			{
				temp=n*count;
				count++;
			}
			else
			{
				cout<<"Case #"<<k<<": "<<(count-1)*n<<"\n";
				break;
			}
		}
		k++;
	}
	return 0;
}
