#include"stdafx.h"

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define mod2 1000000007
#define asitis 1
#define change 0
vector<vector<int> > num;
vector<int> nm;

void gen(int idx, int n)
{
	if (idx >= n)
		return;
	if (idx == n-1)
	{
		nm.push_back(1);
		num.push_back(nm);
		nm.pop_back();
		return;
	}
	nm.push_back(1);
	gen(idx + 1, n);
	nm.pop_back();
	nm.push_back(0);

	gen(idx + 1, n);
	nm.pop_back();

}
vector<ll> bs[12];
vector<int> dv;

int main()
{
	int t, i, j,m;ll n;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> t;
	int len;
	cin >> n >>len ;

	nm.push_back(1);
	gen(1, n);
	
	//cout << num.size();
	ll k = 0,po;
	for (i = 0; i < num.size(); i++)
	{
		
		for (m = 2; m <= 10; m++)
		{
			k = 0; po = 1;
			for (j = num[i].size()-1; j>=0; j--)
			{
				//cout << num[i][j];

				if (num[i][j] == 1)
					k += po;
				po *= m;
			}
			//cout <<"k="<<k<< "\n";
			bs[m].push_back(k);
		}
	}

	printf("Case #1:\n");
	for (i = 0; (i < (bs[2].size()))&&(len); i++)
	{
		dv.clear();
		for (j = 2; j <= 10; j++)
		{
			for (m = 2; m < min((ll)100000,bs[j][i]-1); m++)
			{
				if ((bs[j][i] % m)==0)
				{
					dv.push_back(m);
					break;
				}
			}
		}
		
		if (dv.size() == 9)
		{
			len--;
			for (j = 0; j < num[i].size(); j++)
				cout << num[i][j];
			cout << " ";
			for (j = 0; j < dv.size(); j++)
				cout << dv[j] << " ";
			cout << "\n";
		}


	}
	
	
	

	return 0;
}