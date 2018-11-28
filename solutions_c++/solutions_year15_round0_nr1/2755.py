#include <iostream>
#include <math.h>

using namespace std;


int NeedFriend(int max_level, int audience) {
	int need_add = 0;
	int have = 0;
	for (int i =  0; i <= max_level; ++i) {
		int kth = audience / pow(10, max_level - i);
		if (have >= i) {
			have += kth;
		} else {
			need_add += i - have;
			have = i + kth;
		}
		audience -= kth * pow(10, max_level - i);
	}
	return need_add;
}




int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		int max_level;
		cin >> max_level;
		int audience;
		cin >> audience;
		cout << "Case #" << i + 1 << ": " << NeedFriend(max_level, audience) << endl;
		
	}
	return 0;
}