#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<map>
using namespace std;

int main() {
	//FILE *fin = freopen("B-small-attempt0.in", "r", stdin);
	FILE *fin = freopen("B-large.in", "r", stdin);
	assert(fin != NULL);
	//FILE *fout = freopen("B-small-attempt0.out", "w", stdout);
	FILE *fout = freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int result;
		int numFirst = 0;
		int numSecond = 0;
		//char chr;
		string input;
		cin >> input;
		if (input.size() >= 1)
		{
			char first = input[0];
			char pre = first;
			//cin >> chr;
			//first = chr;
			//pre = first;
			numFirst++;
			//while (cin >> chr)
			for (int i = 1; i < input.size(); i++)
			{
				if (input[i] != pre&&input[i] == first)
					numFirst++;
				else if (input[i] != pre&&input[i] != first)
					numSecond++;
				pre = input[i];
			}
			if (first == '-') result = (numFirst - 1) * 2 + 1;
			else result = numSecond * 2;

			cout << "Case #" << t << ": ";
			cout << result << endl;
		}
		else
		{
			cout << "Case #" << t << ": ";
			cout << 0 << endl;
		}

	}
	exit(0);
}