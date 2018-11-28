// main.cpp

#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <numeric>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <utility>

#define i64 long long
#define ui64 unsigned long long

using namespace std;

#define READ_IN_FILE 1

#ifdef ONLINE_JUDGE
#define READ_IN_FILE 0
#endif

vector<int> vi;
vector<string> si;

double solve()
{
	return 0;
}

int main()
{
    if (READ_IN_FILE) freopen("in.in", "r", stdin);
	
    int T;
    scanf("%d\n", &T);
    if (!T) {
        cerr << "Check input!" << endl;
        exit(0);
    }
    
    for (int t = 1; t <= T; t++) {
		int n = 0, stand = 0, need = 0;
		scanf("%d ", &n);
		for (int sh = 0; sh <= n; sh++) {
			char chr;
			scanf("%c", &chr);
			int c = chr - 48;
			
			if (sh == 0) {
				stand += c;
			} else {
				if (stand < sh) {
					need += (sh - stand);
					stand += c + sh - stand;
				} else {
					stand += c;
				}
			}
		}
		printf("Case #%d: %d\n", t, need);
	}
	
    if (READ_IN_FILE) fclose(stdin);
    return 0;
    
}
