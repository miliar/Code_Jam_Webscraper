#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
#define MOD 1000000007
#define INF 999999999
using namespace std;


const int MAX=10000007;
bool isprime[MAX] = {};
void seive()
{
	int i,j;
	isprime[0]=1;
	isprime[1]=1;
	for(i=2;i*i<MAX;i++)
	{
		if(isprime[i]==0)
		{
			j=i*i;
			for(;j<MAX;j+=i)
				isprime[j]=1;
		}
	}
}

ll convert(string s, int base)
{
	reverse(s.begin(), s.end());
	ll mul = 1;
	ll ret = 0;
	for(int i=0;i<s.size();i++)
	{
		ret += (s[i] - '0') * mul;
		mul *= base;
	}
	return ret;
}
int main()
{
	int tc;
	cin >> tc;
	cout << "Case #1:\n";
	int n,jam;
	cin >> n >> jam;
	ll start = ( 1 << (n-1) ) + 1;
	ll end = ( 1 << (n) ) - 1;
	vector<ll>fin[55];
	int it = 1;
	for(int i=start; i<=end; i+=2)
	{
		string s = "";
		for(int j=0;j<log2(i);j++)
		{
			if(i & (1 << j)) s += '1';
			else s += '0';
		}
		vector<ll>v;
		vector<ll>ans;
		ans.push_back(convert(s, 10));
		//cout << s << " -- ";
		bool found = false;
		for(int j=2; j<=10; j++)
		{
			found = false;
			ll temp = convert(s, j);
			v.push_back(temp);
			//cout << temp << " ";
			if(temp % 2 == 0)
			{
				ans.push_back(2);
				found = 1;
			}
			else
			{
				for(int k=2;k<1000;k++)
				{
					if(temp % k == 0)
					{
						ans.push_back(k);
						found = 1;
						break;
					}
				}
			}
			if(!found) break;
		}
		if(found) fin[it++] = ans;
		//cout << endl;
		if(it > jam) break;
	}
	
	for(int i=1;i<it;i++)
	{
		for(int j=0;j<fin[i].size();j++) cout << fin[i][j] << " ";
		cout << endl;
	}
}
