// created by: Prashant Kumar Singh :)
#include<iostream>
#include<algorithm>
#include<utility>
#include<cstring>
#include<string.h>
#include<set>
#include<map>
#include<math.h>
#include<stdio.h>
#include<vector>
#include<functional>
#include<bitset>
#include<iomanip>
#define ll long long
#define gr greater<ll>()
#define pi acos(-1.0)
#define pb push_back
#define MS0(ar) memset(ar,0,sizeof ar)
#define f first
#define pii pair<int,int>
#define pll pair<ll,ll>
#define ind(a) scanf("%d",&a)
#define inf(a) scanf("%lf",&a)
#define inl(a) scanf("%lld",&a)
#define ins(a) scanf("%s",a)
#define pd(a) printf("%d\n",a)
#define pl(a) printf("%lld\n",a);
#define bitcnt(x) __builtin_popcountll(x)
using namespace std;
char ch[16];
ll ret(ll no)
{
	for (int i = 2; i <= sqrt(no); i++)
	{
		if (no % i == 0)
			return i;
	}
	return 1;
}
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
/*#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
#endif
	freopen("output.txt", "w", stdout);*/
	ll t, k = 0, n, cnt = 0, j;
	string s;
	cin >> t;
	while (t--)
	{
		k++;
		cin >> n >> j;
		cout << "Case #" << k << ": \n";
		//vector<int>v;
		for (int mask = 0; mask < (1 << (n)) && cnt < j; mask++)
		{
			if (mask & 1 && mask & (1 << n - 1))
			{
				int y = mask;
				string str = "";
				while (y > 0)
				{
					int x = y % 2;
					str += (char)(x + 48);
					y /= 2;
				}
				//cout << str << "????" << endl;
				//cout << mask << "djfkvkrf " << endl;
				for (int i = n - 1; i >= 0; i--)
				{
					ch[i] = str[n - 1 - i];
				}
				vector<ll>v;
				for (int i = 2; i <= 10; i++)
				{
					ll b = 1, no = 0;
					for (int j = n - 1; j >= 0; j--)
					{
						//cout<<ch[i];
						no = no + ((ch[j] - 48) * b);
						//cout<<no<<"SSD\n";
						//cout<<b<<"&&& "<<endl;
						b = b * i;
					}
					//cout << no << " ";
					if (ret(no) != 1)
						v.pb(ret(no));
				}
				//cout << endl;
				if (v.size() == 9)
				{
					for (int i = 0; i < n; i++)
						cout << ch[i];
				//cout << endl;
					cnt++;
					cout<<" ";
					for (int i = 0; i < v.size(); i++)
						cout << v[i] << " ";
					cout << endl;
				}
				else
				{
					continue;
				}
				//cout << endl;
			}

		}
	}

	return 0;
}