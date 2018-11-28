//Author: sagarkaniche
#include <bits/stdc++.h>
#define ll long long
using namespace std;
#define si(x) scanf("%d",&x)
#define sdb(x) scanf("%lf",&x)
#define sll(x) scanf("%lld",&x)
#define pb push_back
#define res 1000000007
typedef pair<int,int> pp;



int main()
{
	int t;
	si(t);
	printf("Case #1:\n");
	while(t--)
	{
		ll n,i,J,j,m,tot=0;
		sll(n);sll(J);
		ll x = 1<<(n-1);
		x++;
		ll maxx = 1<<(n-2);
		for(i=0;i<maxx;i++)
		{

			ll val = i*2+x;
			std::vector<int> vec;
			for(j=2;j<=10;j++)
			{
				for(m=2;m<100;m++)
				{
					ll temp=val;
					ll sum = 0,ind=1;
					while(temp)
					{
						if(temp%2==1) sum = (sum + ind)%m;
						temp/=2;
						ind*=j; 
					}
					if(sum==0) {vec.pb(m);break;}
				}
			}
			if(vec.size()==9)
			{
				tot++;
				if(n==16) cout<<bitset<16>(val)<<" ";
				else cout<<bitset<32>(val)<<" ";
				for(int l=0;l<9;l++) printf("%d ",vec[l]); printf("\n");
				if(tot==J) break;
			}
		}

	}
	return 0;
}