#include <iostream>
#include <algorithm>
using namespace std;

#define LEN 1005
int T, N;
double s1[LEN], s2[LEN];
int x, y;
bool cmp(double x, double y) {
	return x > y;
}

int main() {
	cin >> T;
	int cas = 0;
	while (T --) {
		x = 0; y = 0;
		cin >> N;
		for (int i = 0; i < N; i ++)
			cin >> s1[i];
		for (int i = 0; i < N; i ++)
			cin >> s2[i];
		sort(s1, s1 + N, cmp);
		sort(s2, s2 + N, cmp);

		//for (int i = 0; i < N; i ++) cout << s1[i] << ' ';
		//cout << endl;
		//for (int i = 0; i < N; i ++) cout << s2[i] << ' ';
		//cout << endl;
		//y -> not cheat, x -> cheat
		int _head = 0;
		for (int i = 0; i < N; i ++)
			if (s1[i] > s2[_head])
				y ++;
			else
				_head ++;
		int _tail = N-1;
		for (int i = N - 1; i >= 0; i --) {
			if (s1[i] > s2[_tail]) {
				x ++;
				_tail --;
			}
		}
		//for (int i = 0; i < N; i ++)
		//	if (s1[i] > s2[_tail]) {
		//		x ++;
		//		_tail --;
		//	}
		//	else _tail --;
		cout << "Case #" << ++cas << ": " << x << ' ' << y << endl;
	}
	return 0;
}
