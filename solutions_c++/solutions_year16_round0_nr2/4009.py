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

char str[109];

int solve(int i, int j) {
    j--;
    while(j >= i && str[j] == '+')
        j--;
    if(j == i - 1)
        return 0;
    j++;
    int k = j - 1;
    while(k >= i && str[k] == '-')
        k--;
    if(k == i - 1)
        return 1;
    k++;
    return solve(i, k) + 2;
}

int main() {
    int test;
    scanf("%d\n", &test);
    for(int t = 1; t <= test; t++) {
        scanf("%s", str);
        int N = strlen(str);
        printf("Case #%d: %d\n", t, solve(0, N));
    }

    return 0;
}
