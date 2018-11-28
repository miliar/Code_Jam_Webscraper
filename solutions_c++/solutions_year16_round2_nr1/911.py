#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MEM(a,b) memset((a),(b),sizeof(a))
const LL INF = 1e9 + 7;
const int N = 1e6 + 10;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ncase;
	cin >> ncase;
	string str;
	int ks = 1;
	while (ncase--)
	{
		cin >> str;
		int a[256];
		MEM(a, 0);
		for (int i = 0; i < str.length(); i++) a[str[i]] ++;
		int ans[10];
		MEM(ans, 0);

		// solve 0 zero;
		int t;
		t = ans[0] = a['Z'];
		for (int i = 0; i < string("ZERO").length(); i++)
		{
			
			a["ZERO"[i]] -= t;
		}

		// solve 4 four
		t = ans[4] = a['U'];
		for (int i = 0; i < string("FOUR").length(); i++)
		{
			a["FOUR"[i]] -= t;
		}
		

		// solve 6 six
		t = ans[6] = a['X'];
		for (int i = 0; i < string("SIX").length(); i++)
		{
			a["SIX"[i]] -= t;
		}

		// solve 8 eight
		t = ans[8] = a['G'];
		for (int i = 0; i < string("EIGHT").length(); i++)
		{
			a["EIGHT"[i]] -= t;
		}

		// solve 3 three
		t = ans[3] = a['H'];
		for (int i = 0; i < string("THREE").length(); i++)
		{
			a["THREE"[i]] -= t;
		}
		
		// solve 2 two
		t = ans[2] = a['W'];
		for (int i = 0; i < string("TWO").length(); i++)
		{
			a["TWO"[i]] -= t;
		}

		// solve 1 one
		t = ans[1] = a['O'];
		for (int i = 0; i < string("ONE").length(); i++)
		{
			a["ONE"[i]] -= t;
		}

		// solve 5 five
		t = ans[5] = a['F'];
		for (int i = 0; i < string("FIVE").length(); i++)
		{
			a["FIVE"[i]] -= t;
		}
		// solve 7 seven
		t = ans[7] = a['S'];
		for (int i = 0; i < string("SEVEN").length(); i++)
		{
			a["SEVEN"[i]] -= t;
		}

		// solve 9 nine
		t = ans[9] = a['I'];
		for (int i = 0; i < string("NINE").length(); i++)
		{
			a["NINE"[i]] -= t;
		}


		// solve 
		printf("Case #%d: ", ks++);
		for (int i = 0; i < 10; i++) while (ans[i]--) putchar(i + '0');
		puts("");
	}

	return 0;
}