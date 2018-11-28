#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

typedef unsigned long long ull;

using namespace std;

int main() {
int tt,n,sum,res,q;
string s;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> tt;
	
	for (int i=1;i<=tt;i++)
	{
		cin >> n >> s;
		
		sum = 0;
		res = 0;
		
		for (int j=0;j<=n;j++)
		{
			q = s[j]-'0';
			
			if (sum<j)
			{
				sum = j;
				res++;
			}
			
			sum += q;
		}
			
		cout << "Case #" << i << ": " << res << endl;
	}
	
	return 0;
}
