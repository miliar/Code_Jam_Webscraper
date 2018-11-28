#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>
#include <deque>
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
	int t,i,l,z;
	string str,str1;
	cin >> t;
	for(z = 1; z<= t; z++)
	{
		cin >> str;
		str1 = "";
		str1 = str1 + str[0];
		l = str.size();
		for(i = 1; i < l; i++)
		{
			if(str[i] >= str1[0])
			{
				str1 = str[i] + str1;
			}
			else
			{
				str1 = str1+ str[i];
			}
		}
		cout << "Case #" << z << ": " << str1 << endl;
	}
	return 0;
}

