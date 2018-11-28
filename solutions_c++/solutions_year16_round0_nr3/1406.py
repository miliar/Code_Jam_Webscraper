#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int n, j,mod;
vector<string>vec;
map<string, vector<long long > > mp;
long long pw(long long x, long long sum) {
	long long res = 1, power = sum, val = x;
	while (power) {
		if (power & 1) {
			res *= val;
			res %= mod;
		}
		val *= val;
		val %= mod;
		power >>= 1ll;
	}
	return res;
}
int m = 0;
void solve(string s)
{

	if ( m<j && s.size() == n-1)
	{

		long long sum = 0;
		bool flag;
		s+='1';
		vector<long long >v;
		for (int i = 2; i <= 10; i++)
		{

			flag = false;

			for (int p = 2; p<14; p++)
			{
			    mod = p;
			    sum = 0;
			    for (int o = s.size() - 1, k = 0; o >= 0; o--, k++)
			    {
				sum += (s[o] - '0')*pw(i, k);
                sum%=p;
                }
				if (sum == 0)
				{
					flag = true;
					v.push_back(p);
					break;
				}
			}
			if(!flag) break;
		}

		if(flag)
        {
            vec.push_back(s);
		mp[s] = v;
		m++;

        }
        return;
	}

	if (m<j)
	{
	   solve(s+'0');
	   solve(s+'1');
	}

}


int main()
{
	freopen("input.txt" , "r", stdin);
	freopen("output.txt" , "w", stdout);

	int t;
	cin >> t;
	cin >> n >> j;

	solve("1");
	cout<<"Case #1:"<<endl;
	for (int i = 0; i<j; i++)
	{
		cout << vec[i];
		for (int j = 0; j< 9; j++) cout << " " << mp[vec[i]][j];
		cout << endl;
	}
	return 0;
}
