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
typedef long long ll;

using namespace std;

ull gcd (ull a, ull b)
{
  ull c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}

ull lcm(ull a, ull b)
{
  return (a*b)/gcd(a,b);
}

int main() {
ull tt,b,m,res,x[1000],y[1000],cust[1000],curr_p,curr_lcm,tot_p;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> tt;
	
	for (ull i=1;i<=tt;i++)
	{
		cin >> b >> m;
		res = 0;
		curr_lcm = 1;
		tot_p = 0;
		
		for (ull j=0;j<b;j++)
		{
			cin >> x[j];
			curr_lcm = lcm(curr_lcm, x[j]);
			//cout << "curr_lcm:" << curr_lcm << endl;
			y[j] = 0;
			cust[j] = 0;
		}
		
		for (ull j=0;j<b;j++)
			tot_p += (curr_lcm / x[j]);
		curr_p = 0;
		
		//cout << "m before:" << m << endl;
		
		m = tot_p + (m%tot_p);
		
		//cout << "tot_p:" << tot_p << " m:" << m << endl;
		
		while (true)
		{
			for (ull k=0;k<b;k++)
			{
				if (y[k]%x[k] == 0)
				{
					y[k] = 0;
					curr_p++;
				}
				
				if (curr_p == m)
				{
					res = k + 1;
					break;
				}
				
				y[k]++;
			}
			
			if (res > 0)
				break;
		}

		cout << "Case #" << i << ": " << res << endl;
	}
	
	return 0;
}
