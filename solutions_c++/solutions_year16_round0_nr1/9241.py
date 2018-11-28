#include <cstdio>
#include <iostream>
using namespace std;

bool update_seen(bool seen[], int & left, int num){
	for (; num > 0; num /= 10){
		int digit = num % 10;
		if (!seen[digit]){
			seen[digit] = true;
			--left;
		}
	}
	return left;
}

int main(){
	FILE * fin, * fout;
	freopen_s(&fin, "A-large.in", "r", stdin);
	freopen_s(&fout, "sheep.out", "w", stdout);

	int run, num, ans, left; bool seen[10];
	cin >> run;
	for (int a = 1; a <= run; ++a){
		cin >> num;
		cout << "Case #" << a << ": ";
		if (num == 0){
			cout << "INSOMNIA" << endl;
			continue;
		}
		memset(seen, false, sizeof(seen));
		for (ans = num, left = 10; update_seen(seen, left, ans); ans += num);
		cout << ans << endl;
	}
	return 0;
}
