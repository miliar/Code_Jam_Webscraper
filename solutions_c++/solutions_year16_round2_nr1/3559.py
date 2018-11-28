#include <cstdio>
#include <cctype>
#include <cstring>
#include <iostream>
using std::cin;
using std::cout;
using std::endl;
#include <vector>
using std::vector;
#include <algorithm>
using std::sort;

int main()
{
	int T;	scanf("%d", &T);
	for(int t = 0; t < T; ++t) {
		printf("Case #%d: ", t + 1);
		char S[2048];	scanf("%s", S);
		int len = strlen(S);
		
		char A[26];
		for(int i = 0; i < 26; ++i)
			A[i] = 0;
		for(int i = 0; i < len; ++i)
			++ A[S[i] - 'A'];
		
		vector<int> phone;
		
		while(A['Z' - 'A']) {	// 0
			--A['Z' - 'A'];
			--A['E' - 'A'];
			--A['R' - 'A'];
			--A['O' - 'A'];
			phone.push_back(0);
		}
		
		while(A['W' - 'A']) {	// 2
			--A['T' - 'A'];
			--A['W' - 'A'];
			--A['O' - 'A'];
			phone.push_back(2);
		}
		
		while(A['U' - 'A']) {	// 4
			--A['F' - 'A'];
			--A['O' - 'A'];
			--A['U' - 'A'];
			--A['R' - 'A'];
			phone.push_back(4);
		}
		
		while(A['X' - 'A']) {	// 6
			--A['S' - 'A'];
			--A['I' - 'A'];
			--A['X' - 'A'];
			phone.push_back(6);
		}
		
		while(A['O' - 'A']) {	// 1
			--A['O' - 'A'];
			--A['N' - 'A'];
			--A['E' - 'A'];
			phone.push_back(1);
		}
		
		while(A['R' - 'A']) {	// 3
			--A['T' - 'A'];
			--A['H' - 'A'];
			--A['R' - 'A'];
			--A['E' - 'A'];
			--A['E' - 'A'];
			phone.push_back(3);
		}
		
		while(A['F' - 'A']) {	// 5
			--A['F' - 'A'];
			--A['I' - 'A'];
			--A['V' - 'A'];
			--A['E' - 'A'];
			phone.push_back(5);
		}
		
		while(A['S' - 'A']) {	// 7
			--A['S' - 'A'];
			--A['E' - 'A'];
			--A['V' - 'A'];
			--A['E' - 'A'];
			--A['N' - 'A'];
			phone.push_back(7);
		}
		
		while(A['N' - 'A']) {	// 9
			--A['N' - 'A'];
			--A['I' - 'A'];
			--A['N' - 'A'];
			--A['E' - 'A'];
			phone.push_back(9);
		}
		
		while(A['E' - 'A']) {	// 8
			--A['E' - 'A'];
			phone.push_back(8);
		}
		
		sort(phone.begin(), phone.end());
		for(vector<int>::iterator it = phone.begin(); it != phone.end(); ++it)
			cout << *it;
		puts("");
	}
	return 0;
}
