#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <assert.h>

using namespace std;

void test()
{
	int K, C, S;
	cin >> K >> C >> S;
	for (int i = 0; i < S; i++) {
		if (i > 0) {
			cout << " ";
		}
		cout << i + 1;
	}
}

int main(int argc, char* argv[])
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		test();
		cout << endl;
	}
	return 0;
}
