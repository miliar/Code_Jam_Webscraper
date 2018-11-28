#include <iostream>
#include <cstdint>

using namespace std;

int main(int argc, char *argv[]) {
	int num, chars;
	cin >> num;
	for (int i = 0; i < num; i++) {
		cin >> chars;
		char c;
		uint64_t res = 0, current = 0;
		for (int l = 0; l <= chars; l++) {
			cin >> c;
			if (l > current) {
				res += l - current;
				current = l;
			}
			current += (c - '0');
		}
		cout << "Case #" << i+1 << ": " << res << endl;
	}
}