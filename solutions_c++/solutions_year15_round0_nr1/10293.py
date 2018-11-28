#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main() {
	int T;
	int smax;
	string str;
	int pepl,wanted;
	cin >> T;

	for(int i=0;i<T;i++) {
		cin >> smax;
		cin >> str;
		pepl = 0;
		wanted = 0;

		for(int j=0;j<=smax;j++) {
			if(str[j]-48 != 0) {
				if(pepl >= j)
					pepl += str[j] - 48;
				else
					wanted += j - pepl, pepl += wanted + str[j] - 48;
			}
		}

		printf("Case #%d: %d\n",i+1,wanted );
	}

	return 0;
}