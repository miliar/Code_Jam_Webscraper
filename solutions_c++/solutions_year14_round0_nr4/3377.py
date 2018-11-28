#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <ctime>

#define Inf 2147483647
#define Pi acos(-1.0)
#define N 1000000
#define LL long long

inline LL Power(int b, int p) { LL ret = 1; for ( int i = 1; i <= p; i++ ) ret *= b; return ret; }
const int dr [] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int dc [] = {0, 1, 1, 1, 0, -1, -1, -1};

#define F(i, a) for( int i = (0); i < (a); i++ )
#define Fs(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fe(i, x) for(typeof (x.begin()) i = x.begin(); i != x.end (); i++)
#define Set(a, s) memset(a, s, sizeof (a))
#define Max(a, b)  (a < b ? b : a)
#define Min(a, b)  (a > b ? b : a)

using namespace std;

int main(int argc, const char ** argv) 
{
	int t;
	cin>>t;
	for (int loop = 0; loop < t; ++loop)
	{
		std::vector<float> naomi, ken;
		int n, W = 0, DW = 0;
		cin>>n;
		for (int i = 0; i < n; ++i)
		{
			float temp;
			cin>>temp;
			naomi.push_back(temp);
		}
		for (int i = 0; i < n; ++i)
		{
			float temp;
			cin>>temp;
			ken.push_back(temp);
		}
		// naomi score DW
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int cursor = 0;
		for (int i = 0; i < n; ++i)
		{
			if (naomi[i] > ken[cursor])
			{
				DW++;
				cursor++;
			} else {
			}
		}
		// consume ken's largest (bigger than )
		// naomi score W

		// sort(naomi.begin(), naomi.end(), std::greater<float>());
		// sort(ken.begin(), ken.end(), std::greater<float>());
		// cursor = 0;
		// for (int i = 0; i < n; ++i)
		// {
		// 	// cout<<naomi[i]<<endl;
		// 	if (naomi[i] > ken[cursor])
		// 	{
		// 		W++;
		// 	} else {
		// 		cursor++;
		// 	}
		// 	if (i+i-cursor == n-1) break;
		// }

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		cursor = 0;
		for (int i = 0; i < n; ++i)
		{
			if (ken[i] > naomi[cursor])
			{
				W++;
				cursor++;
			} else {
			}
		}

		// naomi choose from big to small. ken: if bigger, choose smallest

		printf("Case #%d: %d %d\n", loop+1, DW, n-W);
	}
    return 0;	
}

// | Naomi | Ken  |
// | 0.02  | 0.06 |
// | 0.15  | 0.08 |
// | 0.27  | 0.29 |
// | 0.54  | 0.31 |
// | 0.58  | 0.46 |
// | 0.62  | 0.50 |
// | 0.67  | 0.52 |
// | 0.75  | 0.73 |
// | 0.79  | 0.81 |
// | 0.88  | 0.96 |

// | Naomi | Ken   |
// | 0.170 | 0.075 |
// | 0.208 | 0.142 |
// | 0.255 | 0.651 |
// | 0.340 | 0.708 |
// | 0.377 | 0.717 |
// | 0.623 | 0.745 |
// | 0.632 | 0.830 |
// | 0.670 | 0.906 |
// | 0.698 | 0.915 |
// | 0.821 | 0.953 |

// | Naomi | Ken   |
// | 0.186 | 0.215 |
// | 0.300 | 0.271 |
// | 0.389 | 0.341 |
// | 0.557 | 0.458 |
// | 0.832 | 0.520 |
// | 0.899 | 0.521 |
// | 0.907 | 0.700 |
// | 0.959 | 0.728 |
// | 0.992 | 0.916 |