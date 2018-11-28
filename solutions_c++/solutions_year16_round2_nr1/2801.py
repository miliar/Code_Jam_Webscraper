#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cstring>
#include <climits>
#include <map>
#include <vector>
#include <queue>
#include <string>

#define	mp	make_pair
#define	MAX	1000000

using namespace std;
int a[26];
const char del[10] = {'Z','W','U','X','G','F','S','O','T','I'};
const string nums[10] = {"ZERO", "TWO", "FOUR", "SIX", "EIGHT", "FIVE", "SEVEN", "ONE", "THREE", "NINE"};
const int intNums[10] = { 0, 2, 4, 6, 8, 5, 7, 1, 3, 9};
int cnt[10];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int t = 0; t < test; t++) {
		memset(cnt, 0, 10*sizeof(int));
		memset(a, 0, 26*sizeof(int));
		
		string s;
		cin >> s;
		for (int i = 0; i < s.size(); i++)
			a[s[i]-'A']++;
		
		
		for (int i = 0; i < 10; i++) {
			if (a[del[i] - 'A']) {
				cnt[intNums[i]] = a[del[i] - 'A'];
				for (int k = 0; k < nums[i].size(); k++)
					a[nums[i][k] - 'A'] -= cnt[intNums[i]];
			}
		}
		cout << "Case #" << t+1 << ": ";
		for (int i = 0; i < 10; i++)
			for (int j = 0; j < cnt[i]; j++)
				cout << i;
		cout << "\n";
	}
	//system("pause");
    return 0;
}