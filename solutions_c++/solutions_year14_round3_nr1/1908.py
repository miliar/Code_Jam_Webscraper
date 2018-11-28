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
#include <fstream>

using namespace std;

int main()
{
	freopen ("input1.txt","r",stdin);
	freopen ("output.txt","w", stdout);
	long long int a=1099511627776, b;
	int T, P, Q, t;
	char d;
	cin >> T;
	for (int e=1; e <= T; e++ )
	{
		cin >> P >> d >> Q;
		b=a*P/Q*Q/P;
		if (a!=b)
		cout << "Case #"<< e << ": impossible" << endl;
		else
		{
			int p=0;
			for ( ; ;)
			{
				p++;
				Q/=2;
				if (P>=Q) 
				{
					cout << "Case #"<< e << ": " << p << endl;
					break;
				}
			}
		}
		
	}
	return 0;
}
