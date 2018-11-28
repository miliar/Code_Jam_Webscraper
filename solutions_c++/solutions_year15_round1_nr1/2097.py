/*
**
**  Author : Lawrence
**  gcjround1.cpp
*/
#include <ios>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cerrno>
#include <cfloat>
#include <cstdio>
#include <cwchar>
#include <iosfwd>
#include <limits>
#include <locale>
#include <memory>
#include <string>
#include <vector>
#include <cassert>
#include <ciso646>
#include <climits>
#include <clocale>
#include <complex>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <cwctype>
#include <fstream>
#include <iomanip>
#include <istream>
#include <numeric>
#include <ostream>
#include <sstream>
#include <utility>
#include <iostream>
#include <iterator>
#include <valarray>
#include <algorithm>
#include <exception>
#include <stdexcept>
#include <streambuf>
#include <functional>
#define Scanf(n) while(~scanf("%d",&n))
#define ll long long
#define lson l, m, rt<<1
#define rson m+1, r, rt<<1|1
#define PI 3.1415926535897932626
#define EXIT exit(0);
#define DEBUG puts("Here is a BUG");
#define Clear(name, init) memset(name, init, sizeof(name))
#define For(i,n) for(int i = 0;i < n; i++)
#define FoR(i,n) for(int i = 1;i <= n; i++)
const double eps = 1e-8;
const int MAXN = (int)1e9 + 5;
using namespace std;
const int M = 1005;
int mus[M];

int main(int argc, char const *argv[]) {

    freopen("/home/lawrence/A-large.in","r+",stdin);
    freopen("/home/lawrence/out.txt","w+",stdout);
	int t;
	while(~scanf("%d",&t)){
		for(int cas = 1;cas <= t; cas++){
			int n;
			scanf("%d",&n);
			int speed = -1;
			for(int i = 0;i < n; i++){
				scanf("%d",&mus[i]);
				if(i == 0)
					continue;
				int temp = mus[i-1] - mus[i];
				if(temp > speed)
					speed = temp;
			}
			int ans1 = 0, ans2 = 0;
			for(int i = 1;i < n; i++){
				if(mus[i] < mus[i-1])
					ans1 += mus[i-1] - mus[i];
			}
			for(int i = 0;i < n-1; i++){
				if(mus[i] < speed)
					ans2 += mus[i];
				else
					ans2 += speed;
			}
			printf("Case #%d: %d %d\n", cas, ans1, ans2);
		}
	}
    return 0;
}

