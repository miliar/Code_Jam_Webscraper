// insomnia.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"

using namespace std;

FILE* stream;
FILE* stream2;

int main()
{
	errno_t err;
	err = freopen_s( &stream, "A-large.in", "r", stdin);


	errno_t err2;
	err2 = freopen_s(&stream2, "A-large.out", "w", stdout);

	int inputcnt = 0;
	cin >> inputcnt;

	int out, base[200], next[200];

	for (int i = 0; i < inputcnt; i++) {
		out = 0;
		cin >> base[i];

		cout << "Case #" << i + 1 << ": ";

		bool chk[10] = {};

		if (base[i] == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		
		
		bool bRepeat = false;
		int n = 1;
		do {
			next[i] = n * base[i];

			while ( next[i] != 0 )
			{
				int nDigit = next[i] % 10;
				chk[nDigit] = true;
				next[i] = next[i] / 10;
			}


			bRepeat = false;
			for (int j = 0;j < 10;j++) {
				if (!chk[j]) bRepeat = true;
			}
			if (bRepeat ) n++;
		} while (bRepeat) ;

		cout << n * base[i] << endl;
	}
	fclose(stream);
	fclose(stream2);
    return 0;
}

