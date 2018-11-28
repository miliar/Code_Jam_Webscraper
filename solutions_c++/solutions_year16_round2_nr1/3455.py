
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

bool r(string &s, int *chr_cnt, string &result) {
    bool finish = true;
    for (int i = 0; i < 26; i++) {
        if (chr_cnt[i] != 0) {
            finish = false;
            break;
        }
    }

    if (finish)
        return true;
    
    for (int i = 0; i < 10; i++) {
        bool skip_word = false;
        
        for (int l = 0; l < 26; l++) {
            if (dict_cnt[i][l] > chr_cnt[l]) {
                skip_word = true;
                break;
            }
        }

        if (skip_word) continue;
        
        // Match
        result.push_back(i + '0');
        
        for (int lt = 0; lt < 26; lt++) {
            chr_cnt[lt] -= dict_cnt[i][lt];
        }
        
        if (r(s, chr_cnt, result)) return true;
        
        result.pop_back();
        
        for (int lt = 0; lt < 26; lt++) {
            chr_cnt[lt] += dict_cnt[i][lt];
        }
    }
    return false;
}


string solve(string s) {
    string result;
    
    int chr_cnt[26] = {0};
    
    if (first) {
        first = false;
        for (int i = 0; i < 10; i++) {
            for (char c : dict[i]) {
                dict_cnt[i][c - 'A']++;
            }
        }
    }

    for (char c : s) chr_cnt[c - 'A']++;
    
    r(s, chr_cnt, result);
    
    sort(result.begin(), result.end());
    
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

        string s;
        getline (cin, s);
        
        printf("Case #%d: %s\n", t, solve(s).c_str());
    }
	
    
	if (READ_IN_FILE) fclose(stdin);
	return 0;
}
