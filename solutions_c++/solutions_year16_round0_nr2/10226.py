/*
 * @author:metastableB
 * B_revenge_of_the_pancakes.cpp
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
int get_char(string s, int a, char c){
	int i = a, ret = 0;
	while(s[i] == c && i < s.size()) {ret++;i++;}
	return ret;
}

int main() {
	long int a, b, T;
	cin >> T;
	int cse = 1;
	while(cse <= T){
		string s = "";
		cin >> s;
		//std::cout << "s";
		int a =0, b =0;
		int flip = 0;
		char c;
		a = a + get_char(s,a,'+');
		while(a < s.length()){
			a = a + get_char(s,a,'+');
			b = get_char(s,a,'-');
			//cout << "a " << a <<" b " << b << "\n";
			if(a > 0) flip += 1;
			if(b > 0) flip += 1;
			a = a + b;
			a = a + get_char(s,a,'+');
			//cout << flip << " " << a << "\n";
			//cin >> c;
		}
		cout << "Case #" << cse << ": " << flip << "\n";
		cse++;
	}
    return 0;
}
