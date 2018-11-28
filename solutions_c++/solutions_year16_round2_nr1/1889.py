#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>
#include <utility>
#include <functional>
#include <cstring>
#include <queue>
#include <stack>
#include <math.h>
#include <iterator>
#include <vector>
#include <string>
#include <set>
#include <math.h>
#include <iostream> 
#include<map>
#include <stdlib.h>
#include <list>
#include <typeinfo>
#include <list>
#include <set>
using namespace std;
#include <cstdint>
#define M_PI 3.1415926535897932384626433832795
#define MAX_MOD 1000000007
#define REP(i,n) for(int i = 0;i < n;++i)
int hoge[10000] = {};
int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1;i <= t;++i) {
		cout << "Case #" << i << ": ";
		string s;
		cin >> s;
		for (int q = 0;q < s.length();++q) {
			hoge[(int)s[q]]++;
		}
		int zero = hoge[(int)'Z'];//0
		hoge[(int)'Z'] -= zero;
		hoge[(int)'E'] -= zero;
		hoge[(int)'R'] -= zero;
		hoge[(int)'O'] -= zero;
		int four = hoge[(int)'U'];//4
		hoge[(int)'F'] -= four;
		hoge[(int)'O'] -= four;
		hoge[(int)'U'] -= four;
		hoge[(int)'R'] -= four;
		int six = hoge[(int)'X'];
		hoge[(int)'S'] -= six;
		hoge[(int)'I'] -= six;
		hoge[(int)'X'] -= six;
		int seven = hoge[(int)'S'];
		hoge[(int)'S'] -= seven;
		hoge[(int)'E'] -= 2 * seven;
		hoge[(int)'V'] -= seven;
		hoge[(int)'N'] -= seven;
		int five = hoge[(int)'V'];
		hoge[(int)'F'] -= five;
		hoge[(int)'I'] -= five;
		hoge[(int)'V'] -= five;
		hoge[(int)'E'] -= five;
		int eight = hoge[(int)'G'];
		hoge[(int)'E'] -= eight;
		hoge[(int)'I'] -= eight;
		hoge[(int)'G'] -= eight;
		hoge[(int)'H'] -= eight;
		hoge[(int)'T'] -= eight;
		int three = hoge[(int)'H'];
		hoge[(int)'T'] -= three;
		hoge[(int)'H'] -= three;
		hoge[(int)'R'] -= three;
		hoge[(int)'E'] -= 2 * three;
		int nine = hoge[(int)'I'];
		hoge[(int)'N'] -= nine*2;
		hoge[(int)'I'] -= nine;
		hoge[(int)'E'] -= nine;
		int two = hoge[(int)'W'];
		hoge[(int)'W'] -= two;
		hoge[(int)'T'] -= two;
		hoge[(int)'O'] -= two;
		int one = hoge[(int)'N'];
		hoge[(int)'N'] -= one;
		hoge[(int)'O'] -= one;
		hoge[(int)'E'] -= one;
		REP(q, zero) {
			cout << "0";
		}
		REP(q, one) cout << "1";
		REP(q, two) cout << "2";
		REP(q, three) cout << "3";
		REP(q, four) cout << "4";
		REP(q, five) cout << "5";
		REP(q, six) cout << "6";
		REP(q, seven)  cout << "7";
		REP(q, eight) cout << "8";
		REP(q, nine) cout << "9";
		cout << endl;
	}
}