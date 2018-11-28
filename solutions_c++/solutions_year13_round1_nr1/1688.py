#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>


using namespace std;

void solve()
{
	long long r, t;
	cin >> r >> t;
	long long i = 0;
	long long area = 0;
	long long sign = -1;
	while (area <= t) {
		area += sign * (r + i) * (r + i);
		if (area <= t) {
			i++;	
		}
		sign = -sign;
	}
	cout << i/2 << endl;
}

int main(int argc, char *argv[]) {
	freopen("in.txt","r",stdin);
	freopen("o.txt","w",stdout);
	int T;
	cin >> T;
	int k = 0;
	while (T--) {
		cout << "Case #" << ++k <<": ";
		solve();
	}
	return 0;	
}