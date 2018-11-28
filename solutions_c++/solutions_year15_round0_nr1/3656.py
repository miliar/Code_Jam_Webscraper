#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define debug 01
#define openfile freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout)

typedef long long ll;
typedef pair<int, int> pii;

int test;

int main() {
	if (debug) openfile;
	cin >> test;
	int n;

	for (int ii=0; ii<test; ii++) {
		int numberOfFriends = 0;
		int numberOfPeopleClap = 0;
		cin >> n;
		char c;		
		for (int i = 0; i < n + 1; i++) {		
			cin >> c;
			int a = c - 48;
			if (i != 0) {
				if (numberOfPeopleClap < i) {
					numberOfFriends += (i - numberOfPeopleClap);
					a += (i - numberOfPeopleClap);
				}
			}
			numberOfPeopleClap += a;
		}
		cout << "Case #" << ii + 1 << ": " << numberOfFriends << endl;
	}
	
	

}
