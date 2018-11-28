// revenge.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

FILE* stream;
FILE* stream2;

void flipSign(char* sign, int fibot) {

	for (int i = 0; i <= fibot; i++) {
		if (sign[i] == '+') sign[i] = '-';
		else if (sign[i] == '-') sign[i] = '+';
	}
}

bool ishappy(char* sign) {
	for (int i = 0; i < 200; i++) {
		if (sign[i] == '-') return false;
	}

	return true;
}

int main()
{
	errno_t err;
	err = freopen_s(&stream, "B-large.in", "r", stdin);


	errno_t err2;
	err2 = freopen_s(&stream2, "B-large.out", "w", stdout);

	int inputcnt = 0;
	cin >> inputcnt;

	for (int i = 0; i < inputcnt; i++) {
		char sign[200] = {};
		cin >> sign;
		int flip = 0;
		while (!ishappy(sign))
		{
			long fibot = 0;

			char first = sign[0];
			for (int j = 1; j < 200; j++ ) {
				if (sign[j] != first) break;
				fibot++;
			}

			flipSign(sign, fibot);

			flip++;
		}
		cout << "Case #" << i+1 << ": " << flip << endl;


	}
	fclose(stream);
	fclose(stream2);
	return 0;
}

