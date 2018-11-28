#include <string>
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

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 1; i <= n; ++i) {
	int A, B, K;
	
	cin >> A >> B >> K;

	int res = 0;
	for (int j = 0; j < A; ++j) {
	    for (int k = 0; k < B; ++k) {
		if ((j & k) < K)
		    res++;
	    }
	}

	cout << "Case #" << i << ": " << res << endl;
    }

    return 0;
}
