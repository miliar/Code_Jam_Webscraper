#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> PLL;
const int MAXN = 100000005;


bool prime[MAXN];
vector<ll>primes;
int sz;


void sieve()
{
	int i , j;

	for(i = 2 ; i <= sqrt(MAXN) ; i++)
	{
		if(prime[i] == false)
		{
			for(j = 2*i ; j < MAXN ; j += i)
			{
				prime[j] = true;
			}
		}
	}

	for(i = 2 ; i < MAXN ; i++)
	{
		if(!prime[i])
			primes.push_back((ll)i);
	}

	sz = primes.size();
}

ll Convert_ToNumber(string s, ll base)
{
	ll ret = 0LL, b = 1;

	for(int i =15  ; i >= 0 ; i--)
	{
//		cout<<i<<" "<<s[i]<<" "<<b<<endl;
		if(s[i] != '0')
			ret += b;
		b *= base;
	}

	return ret;
}

string Convert_ToString(ll num)
{
	string ret = "";
	for(int i = 15 ; i >= 0 ; i--)
	{
		ll x = pow(2LL, i);
		ll y = num/x;
		if(y > 0)
		{
			ret += '1';
			num -= x;
		}
		else
			ret += '0';
	}
	return ret;
}

ll Check_Prime(ll num)
{
	int i ;
	for(i = 0 ; i < sz && primes[i] < num ;i++)
	{
		if(num%primes[i] == 0)
			return primes[i];
	}
	return -1LL;
}

void solve()
{
	cout<<"Case #1:"<<endl;
	ll i, num;
	ll start = 32769LL;
	int cnt = 0;
	bool flag = true;
	vector<ll>v;

	while(true)
	{
		flag = true;
		v.clear();
		string s = Convert_ToString(start);
		for(i = 2 ; i <= 10 ; i++)
		{
			num = Convert_ToNumber(s, i);
			ll x = Check_Prime(num);
			if(x == -1LL)
			{
				flag = false;
				break;
			}
			else
				v.push_back(x);
		}
		if(flag)
		{
			cnt++;
			cout<<s<<" ";
			for(i = 0 ; i < 9 ; i++)
				cout<<v[i]<<" ";
			cout<<endl;
		}
		
		if(cnt == 50)
			break;
		start += 2;
	}
	return;
}

int main()
{
	sieve();
	solve();
	return 0;
}