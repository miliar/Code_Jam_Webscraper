#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <string>
#include <set>
#include <limits.h>

#define inp(x) scanf("%d",&x)
#define inp_l(x) scanf("%lld",&x)
#define inp_d(x) scanf("%lf",&x)
#define MOD 1000000007

using namespace std;


typedef long long int ll;
typedef vector <int> VI;
typedef vector <long long int> VLL;
typedef pair<int,int> PI;
typedef pair<ll,ll> PLL;

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	int t,i,j,k,l,z,ans;
	char c;
	cin >> t;
	string str,str1;
	for(z = 1; z <= t; z++)
	{
		cin >> str;
		str1="";
		i = 0;
		l = str.size();
		while(i < l)
		{
			c = str[i];
			str1 = str1 + c;
			while(i < l && str[i] == c)
			{
				i++;
			}
		}
		l = str1.size();
		//cout << str1 << endl;
		if(str1[l-1] == '+')
		{
			ans = l-1;
		}
		else
		{
			ans = l;
		}
		cout << "Case #" << z << ": " << ans << endl;
	}
	return 0;
}

