/*
 * @author:metastableB
 * A_the_last_word.cpp
 * 
 */

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <climits>
#include <ctime>

/* BEGIN Timer */
#define CLOCK clock()
#define BEGIN_CLOCK clock_t _bx_ = clock();
#define END_CLOCK clock_t _ex_ = clock();
#define TOTAL_C (double)(_ex_ - _bx_)
#define TOTAL_T (TOTAL_C/CLOCKS_PER_SEC)
#define PRINT_CLOCK (printf("%2.3f\n",TOTAL_T));
/* END Timer */
#define ULL unsigned long long
#define LL long long

using namespace std;
string max_l(string s){
	char head = s[0];
	string ret = s.substr(0,1);
	for(int i = 1; i < s.length() ;i++){
		if(s[i]>=head) { head=s[i]; ret = s[i] + ret;}
		else ret = ret + s[i];
	}
	return ret;
}
int main() {
	int T;
	cin >> T;
	int cse = 1;
	while(cse <= T){
		string s;
		cin >> s;
		cout << "Case #" << cse << ": " << max_l(s) << "\n";
		cse++;
	}
    return 0;
}
