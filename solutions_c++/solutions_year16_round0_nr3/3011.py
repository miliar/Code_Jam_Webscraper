#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

typedef long long int ll;

ll  GetNum(ll N, ll k)
{
	ll ans=0;
	ll temp=1;
	while(N)
    {
		if(N&1)
			ans+=temp;
		temp*=k;
		N=N/2;
	}
	return ans;
}

bool checkPrime(ll N)
{
    ll i;
	for(i=2; i*i<=N; i++)
    {
		if(N%i == 0)
			return false;
	}
	return true;
}

void print(ll N)
{
	string S="";
	while(N)
    {
		if(N&1)
            S+='1';
		else
            S+='0';
		N=N/2;
	}
	reverse(S.begin(),S.end());
	cout<<S;
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen ("output.txt","w",stdout);
    int Test,k=0;
	scanf("%lld",&Test);
	while(Test--)
    {
        vector<ll> V;
		int N,J,p,j;
		scanf("%d%d",&N,&J);
		printf("Case #%d:\n",++k);
        ll i=(1LL<<(N-1))+1;
        ll lim=(1LL<<(N));
		for(;i<lim && V.size()<J; i+=2)
        {
			bool flag=false;
			for(int j=2; j<=10; j++)
			{
			    ll temp=GetNum(i,j);
				if(checkPrime(temp))
				{
					flag=true;
					break;
				}
			}
			if(!flag)
                V.push_back(i);
		}
		for(p=0; p<V.size(); p++)
		{
			ll temp=V[p];
			print(temp);
			for(i=2; i<=10; i++)
            {
				ll M=GetNum(temp,i);
				for(int j=2; j*j<=M; j++)
				{
					if(M%j == 0)
					{
						printf(" %d", j);
						break;
					}
				}
            }
            printf("\n");
		}
		printf("\n");
	}
	fclose(stdout);
	return 0;
}
