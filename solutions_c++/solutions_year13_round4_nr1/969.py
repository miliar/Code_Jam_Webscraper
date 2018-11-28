#include <iostream>
#include <sstream>
#include <cstddef>
#include <climits>
#include <functional>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <string.h>

using namespace std;
typedef long long ll;


int T;
const ll mod=1000002013;
ll n,m,num[2000];

int main()
{
	cin>>T;
	for (int CASE = 1; CASE <= T; CASE++)
	{
		cin>>n>>m;

		ll money=0;
		memset(num,0,sizeof(num));
		for (int i = 0; i < m; i++)
		{
			ll a,b,c;cin>>a>>b>>c;
			a--;b--;
			for (int j = a; j <= b-1; j++) num[j]=(num[j]+c)%mod;
			
			ll counter=b-a-1;
			if (counter>=1)
			{
				ll add=((1+counter)*counter)/2;
				money=(money+add*c)%mod;
			}
		}

		ll sum=0;
		for (int i = 0; i < n-1; i++)
		{
			while (num[i]>0)
			{
				ll sub=num[i];
				int index=i;
				for (int j = i+1; j < n-1; j++)
				{
					if (num[j]==0) break;
					sub=min(sub,num[j]);
					index++;
				}

				int counter=index-i;
				if (counter>=1)
				{
					ll add=((1+counter)*counter)/2;
					sum=(sum+add*sub)%mod;
				}
				for (int j = i; j <= index; j++) num[j]-=sub;
			}
		}

		cout<<"Case #"<<CASE<<": "<<((sum+mod-money)%mod)<<endl;
	}

	return 0;
}