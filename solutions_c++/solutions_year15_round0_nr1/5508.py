#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <list>
#include <cctype>
#include <cstdio>
#include <iterator>

using namespace std;

typedef unsigned long long int ll;

int main() {
		
	int t;
	cin >> t;
	for(int k = 0; k < t; ++k) {
		int s;
		string a;
		cin >> s >> a;
		int need_invite = 0, already_stand = 0;
		for(int i = 0; i <= s; ++i) {
			if(i > already_stand + need_invite)
				need_invite += (i - already_stand - need_invite);
			already_stand += a[i] - '0';
		}

		cout << "Case #" << k+1 << ": " << need_invite << endl;
	}



	return 0;
}