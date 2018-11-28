#define  _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <complex>
#include <exception>
#include <list>
#include <stack>
#include <bitset>
#include <csetjmp>
#include <fstream>
#include <locale>
#include <stdexcept>
#include <cassert>
#include <csignal>
#include <functional>
#include <map>
#include <cctype>
#include <cstdarg>
#include <iomanip>
#include <memory>
#include <streambuf>
#include <cerrno>
#include <cstddef>
#include <ios>
#include <new>
#include <string>
#include <cfloat>
#include <cstdio>
#include <iosfwd>
#include <numeric>
#include <typeinfo>
#include <ciso646>
#include <cstdlib>
#include <iostream>
#include <ostream>
#include <utility>
#include <climits>
#include <cstring>
#include <istream>
#include <queue>
#include <valarray>
#include <clocale>
#include <ctime>
#include <iterator>
#include <set>
#include <vector>
#include <cmath>
#include <deque>
#include <limits>
#include <sstream>

typedef long long ll;
typedef unsigned int ui;
#define vi vector<int>
#define vvi vector<vector<int> >
#define vpii vector<pair<int,int> >

#define veceach(v) for(uint i = 0;i < (v).size();i++)
#define veceach2(v,i) for(uint i = 0;i < (v).size();i++)
using namespace std;

vi chars(255), chars_temp;

vi digits(10);

vector<string> txt;


bool rec (int digit) {
	if (digit == 10) {
		if (chars == chars_temp) return true;
		else
			return false;
	}

	digits[digit] = 0;
	if (rec(digit + 1)) return true;

	int n = 0;
	while (true) {
		n++;

		string s = txt[digit];
		for (int i = 0; i < s.length(); i++) {
			chars_temp[s[i]]++;
		}

		bool ok = true;
		for (int i = 0; i < s.length(); i++) {
			if (chars[s[i]] < chars_temp[s[i]]) {
				ok = false;
				break;
			}
		}

		if (!ok) break;

		digits[digit] = n;
		if (rec(digit + 1)) return true;
	}

	for (int j = 0; j < n; j++) {
		string s = txt[digit];
		for (int i = 0; i < s.length(); i++) {
			chars_temp[s[i]]--;
		}
	}

	return false;
}



void main () {
	int T, n;

	FILE *f_in, *f_out;
	f_in = fopen("data.txt","r");	
	f_out = fopen("output.txt","w");	
	fscanf(f_in,"%d",&T);

	txt.push_back("ZERO");
	txt.push_back("ONE");
	txt.push_back("TWO");
	txt.push_back("THREE");
	txt.push_back("FOUR");
	txt.push_back("FIVE");
	txt.push_back("SIX");
	txt.push_back("SEVEN");
	txt.push_back("EIGHT");
	txt.push_back("NINE");
	
	for (int t = 0; t < T; ++t) {
		//fscanf(f_in, "%d", &n);
		
		chars.assign(255, 0);
		chars_temp.assign(255, 0);
		digits.assign(10, 0);

		char buff[3000];

		
			fscanf(f_in, "%s", buff);

			for (int  j = 0; j < strlen(buff); j++) {
				chars[buff[j]]++;
			}
		

		rec(0);


		fprintf(f_out, "Case #%d: ", t+1);

		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < digits[i]; j++) { 
				fprintf(f_out, "%d", i);
			}
		}
		fprintf(f_out, "\n");
	}
	
}