#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>     // std::cout
#include <functional>   // std::minus
#include <numeric>
using namespace std;

int readint() {
	int x;
	cin >> x;
	return x;
}

int main(int argc, char* argv[])
{
	int T = readint();
	for (int t = 0; t < T; t++)
	{
		cout << "Case #" << t + 1 << ": ";
		int friends = 0;

		int Smax = readint();
		string str;
		cin >> str;

		int standing = 0;

		for (int i = 0; i < str.length();) {
			int items = str[i] - '0';

			if (standing >= i) {
				standing += items;
				i++;
			}
			else {
				friends++;
				standing++;
			}

		}


		cout << friends << endl;
	}
	return 0;
}

