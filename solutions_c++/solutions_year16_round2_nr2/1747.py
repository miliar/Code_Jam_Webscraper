
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

string dict[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int dict_cnt[10][26] = {0};
bool first = true;



inline bool validate(string &s, int &n, int &len) {
    stringstream ss;
    ss << setw(len) << setfill('0') <<  n;
    
    string sss = ss.str();
    
    for (int i = 0; i < s.length(); i++) {
        if (s[i] != sss[i] && s[i] != '?') return false;
    }
    return true;
}

string solve(string c, string j) {
    int max = pow(10, c.length());
    int len = c.length();
    
    int min_abs = INT_MAX;
    
    string result;
    
    for(int cc = 0; cc < max; cc++) {
        if (!validate(c, cc, len)) continue;
        for(int jj = 0; jj < max; jj++) {
            int absv = abs(cc - jj);
            if (absv >= min_abs) continue;
            
            if (!validate(j, jj, len)) continue;
            
            min_abs = absv;
            
            stringstream ss;
            ss << setw(len) << setfill('0') << cc << " " << setw(len) << setfill('0') << to_string(jj);
            result = ss.str();
        }
    }
    return result;
}

int main()
{
	if (READ_IN_FILE) freopen("in.in", "r", stdin);
	int T = 0;
	scanf("%d\n", &T);
	if (!T) { cerr << "Check input!" << endl; exit(0); }

    // Each case
	for (int t = 1; t <= T; t++) {

        string c, j;
        cin >> c >> j;
        
        printf("Case #%d: %s\n", t, solve(c, j).c_str());
    }
	
    
	if (READ_IN_FILE) fclose(stdin);
	return 0;
}
