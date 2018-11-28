
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <bitset>
#include <deque>
#include <list>
#include <unordered_map>
#include <unordered_set>
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




string solve(string s) {
    string result;
    
    for (char c : s) {
        if (!result.length() || c < result[0]) {
            result.push_back(c);
        } else {
            result.insert(result.begin(), c);
        }
    }
    return result;
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

        string s;
        getline (cin, s);
        
        printf("Case #%d: %s\n", t, solve(s).c_str());
    }
	
	if (READ_IN_FILE) fclose(stdin);
	return 0;
}
