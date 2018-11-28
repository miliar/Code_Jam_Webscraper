#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <bits/stdc++.h>
#define rep(s , n) for(int i = s ; i < n ; i++)
#define all(x) x.begin() , x.end()
#define CLR( x ) memset(x , 0 , sizeof x)
#define pb push_back
#define ii pair
#define mp make_pair
#define f first
#define s second
#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int j = 0, tc = 0;
	cin >> tc;
	while (tc--) {
		j++;
		string s;
		cin >> s;
		int i = 0, cnt = 0;
		while (i < (int) s.length() - 1) {
			if (s[i] != s[i + 1])
				cnt++;
			i++;
		}
		if (s[s.length() - 1] == '-')
			cnt++;
		cout << "Case #" << j << ": " << cnt << endl;
	}
}
