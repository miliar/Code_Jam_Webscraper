#include<iostream>
#include<sstream>
#include<string>
#include<array>
#include<vector> // vector
#include<map>
#include<utility> //pair
#include<queue> // priority_queue
#include<algorithm>

#include<cstdio>
#include<cmath>
#include<cstring>
#include<functional> // greater

using namespace std;
bool isRwin(int x, int r, int c){
	if (x >= 7) return true;
	if (r*c % x > 0) return true;
	if (max(r, c) < x) return true;
	if (x == 4 && (r == 2 || c == 2)) return true;

	for (int i = 1; i <= x; ++i){
		int j = x + 1 - i;
		// 이렇게 만든 조각이 r*c 안에 들어가지 않으면 탈락시킨다.
		if ((i > r || j > c) && (i > c || j > r))
			return true;
	}

	return false;
}
int main()
{
	freopen("D-small-attempt4.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t; cin >> t;
	for (int i = 1; i <= t; ++i){
		int x, r, c;
		cin >> x >> r >> c;
		string ans = "GABRIEL";
		if (isRwin(x, r, c)){
			ans = "RICHARD";
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}