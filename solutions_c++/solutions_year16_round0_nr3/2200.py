#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

typedef long long ll;
bool check = false;

ll counter=0;
ll temp_arr[10];
bool prime[65537];
ll pre_comp[11][17];
ll n,j;

void comp()
{
	for(ll i=2;i<=10;i++)
	{
		pre_comp[i][0]=1;
		for(ll m=1;m<16;m++)
		{
			pre_comp[i][m] = pre_comp[i][m-1]*i;
		}
	}
	//cout<<" checking now "<<pre_comp[10][0]<<endl;
}

void SieveOfEratosthenes()
{
   // bool prime[n+1];
	ll n = 65536;
    memset(prime, true, sizeof(prime));
 
    for (ll p=2; p*p<=n; p++)
    {
        if (prime[p] == true)
        {
            for (ll i=p*2; i<=n; i += p)
                prime[i] = false;
        }
    }
}

void dfs(string temp_str,ll len)
{
	if(check)
		return;
	else if(len==(n-1))
	{
		counter++;
		temp_str = '1'+temp_str;
		for(int i=2;i<=10;i++)
		{
			temp_arr[i]=0;
		}
		//bool valid=true;
		for(ll i=n-1;i>=0;i--)
		{
			if(temp_str[i]=='1')
			{
				ll k;
				for( k=2;k<=10;k++)
				{
					temp_arr[k] +=pre_comp[k][n-1-i];
				}
			}
		}
		if(1)
		{
			//counter++;
			if(counter==j)
				check=true;
			cout<<temp_str<<temp_str<<" ";
			for(ll i=2;i<=10;i++)
			{
				cout<<temp_arr[i]<<" ";
			}
			cout<<endl;
		}
	}
	else
	{
		string temp = '0'+temp_str;
		dfs(temp,len+1);
		temp = '1'+temp_str;
		dfs(temp,len+1);
	}
}
int main()
{
	ll t;
	scanf("%lld",&t);
	comp();
	//SieveOfEratosthenes();
	while(t--)
	{
		ll n1;
		scanf("%lld",&n1);
		n=n1/2;
		scanf("%lld",&j);
		cout<<"Case #"<<1<<":"<<endl;
		dfs("1",1);
		//cout<<" pre_comp "<<pre_comp[10][0]<<endl;
	}
}