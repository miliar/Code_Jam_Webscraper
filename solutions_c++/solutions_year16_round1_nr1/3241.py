#define __cplusplus 201103L

#include <iostream>
#include <sstream>
#include <fstream>
#include <array>
#include <deque>
#include <forward_list>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <complex>
#include <iterator>
#include <memory>
#include <numeric>
#include <random>
#include <string>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <gmp.h>

using namespace std;

int main() {
	freopen("output.txt", "w", stdout);
	freopen("input.txt", "r", stdin);

	int N;
	string ss;
	const char* s;

	cin>>N;


	for (int i = 0; i < N;i++) {
		if (i != 0)
			cout<<endl;
		cin>>ss;
		s = ss.c_str();
		cerr<<s<<endl;
		int l = strlen(s);
		string o(1, s[0]);
		for(int j=1;j<l;j++) {
			if (s[j] >= o.at(0)) {
				o = string(1, s[j]) + o;
			}
			else {
				o = o+string(1, s[j]);
			}
		}
		//cerr << o<<endl;
		cout<<"Case #"<<i+1<<": "<<o;
	}




	return 0;
}

