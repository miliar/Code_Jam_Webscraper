/* Author: hypothesist */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <iomanip>
#include <ctime>

using namespace std;

#define all(c) (c).begin(), (c).end()

template <typename T> class __cl
{
	public:
		std::vector<T> values;
		void operator()(const T& value)
		{
			if (std::find(all(values), value) == values.end())
				values.push_back(value);
		}
};

typedef istringstream is;
typedef ostringstream os;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;

#define eps 1e-8
#define inf 1e8

#define tr(container, it) for(typeof((container).begin()) it = (container).begin(); it != (container).end(); it++)

#define ex_set(container, element) ((container).find((element)) != (container).end())
#define ex_vec(container, element) (find(all(container), (element)) != (container).end())

#define rm_dupl_s(container) set<typeof(*((container).begin()))> __s(all(container)); (container) = vector<typeof(*((container).begin()))>(all(__s))
#define rm_dupl_us(container) (container) = for_each(all(container), __cl<int>()).values

int seen[10];
int nseen;

void solve(int x) {
    while(x) {
        if(!seen[x%10]) {
            nseen++;
            seen[x%10] = 1;
        }
        x/=10;
    }
}

int main() {
    int test;
    scanf("%d", &test);
    for(int t = 1; t <= test; t++) {
        int n, i;
        scanf("%d", &n);
        if(n == 0) {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }
        for(i = 0; i <= 9; i++)
            seen[i] = 0;
        nseen = 0;
        for(i = n; i <= (1 << 30) - 1 && nseen < 10; i += n)
            solve(i);
        if(nseen == 10)
            printf("Case #%d: %d\n", t, i - n);
    }
}
