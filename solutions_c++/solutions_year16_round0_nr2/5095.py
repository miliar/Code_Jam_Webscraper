#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int
main(int argc, char** argv)
{
	int N, a, n=1;
	cin >> N;
	while(n <= N) {
		string input;
		cout << "Case #" << n << ": ";
		cin >> input;
		int result = 0;
		bool done = false;
		while(!done) {
			int lastMinus = -1;
			for (int i = 0; i < input.size(); i++) {
				if (input[i] == '-') {
					lastMinus = i;
				}
			}

			if (lastMinus == -1) {
				done=true;
			}
			else {
				for (int i=0; i <= lastMinus; i++) {
					if (input[i] == '-') {
						input[i] = '+';
					}
					else {
						input[i] = '-';
					}
				}
				result++;
			}
		}
		cout << result << endl;
		n++;
	} 
	return 0;
}