#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main(){
	FILE * fin, * fout;
	freopen_s(&fin, "A-large.in", "r", stdin);
	freopen_s(&fout, "ovation.out", "w", stdout);
	int run, shy, invite, cur; string cnt;
	cin >> run;
	for (int a = 1; a <= run; ++a){
		cin >> shy >> cnt;
		invite = cur = 0;
		for (int x = 0; x <= shy; ++x){
			for (; cur < x; ++cur, ++invite);
			cur += int(cnt[x] - '0');
		}
		cout << "Case #" << a << ": " << invite << endl;
	}
	return 0;
}
