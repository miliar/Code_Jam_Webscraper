#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<queue>
#include<sstream>

#define INF 1000000000
#define endl '\n'
#define ll long long
#define SS stringstream

using namespace std;

bool used[10];

void parse(ll x)
{
	while(x > 0)
	{
		used[x%10] = true;
		x /= 10;
	}
}

bool check()
{
	for(int i = 0 ; i < 10 ; i++)
		if(!used[i])
			return false;
	return true;
}

string itos(ll a)
{
	string s;
	SS ss;
	ss << a;
	ss >> s;
	return s;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int T;
	cin >> T;
	for(int t=1; t <= T ; t++)
	{
		ll n;
		cin >> n;
		
		string ans;
		if(n==0)
			ans = "INSOMNIA";
		else
		{
			memset(used,0,sizeof(used));
			for(int i=1 ; i < 300 ; i++)
			{
				parse(n*i);
				if(check())
				{
					ans = itos(n*i);
					break;
				}
			}
		}
		
		cout << "Case #" << t << ": " << ans << endl;
	}
	
	return 0;
}

