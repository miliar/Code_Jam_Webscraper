// jamcoin.cpp : 콘솔 응용 프로그램에 대한 진입점을 정의합니다.
//

#include "stdafx.h"
#include <iostream>
#include <set>
using namespace std;

FILE* stream;
FILE* stream2;

std::set<unsigned long long> prime;
static unsigned long long seed = 0;
unsigned long long makeCheck(int digitCnt) {
	unsigned long long check = 0;
	if (seed == 0) seed = rand();
	unsigned long long mul2 = seed;
	for (int j = 0; j < digitCnt; j++) {
		int mul = 0;
		if (j == 0 || j == (digitCnt - 1)) {
			mul = 1;
		}
		else
		{
			mul = mul2 % 2;
			mul2 /= 2;
		}

		check *= 10;
		check += mul;
	}

	seed++;
	return check;
}

unsigned long long ChangeDigit(unsigned long long base, int digit) {
	unsigned long long ret = 0;
	unsigned long long mul = 1;
	while ( base > 0 )
	{
		ret += (base % 10) * mul;
		mul *= digit;

		base /= 10;
	}

	return ret;
}

unsigned long long GetCurMaxPrime() {
	return *prime.rbegin();
}

bool IsPrime(unsigned long long num, unsigned long long& diver ) {
	unsigned long long  i;
	unsigned long long fibot = num / 2;
	for (i = 19; i< fibot; i+= 2)
	{
		if (num % i == 0)
		{
			diver = i;
			return false;
		}
		else {
			fibot = (num / i + 1);
		}
	}
	diver = num;
	return true;

}

int main()
{
	errno_t err;
	err = freopen_s(&stream, "C-small-attempt0.in", "r", stdin);


	errno_t err2;
	err2 = freopen_s(&stream2, "C-small-attempt0.out", "w", stdout);

	int inputcnt = 0;
	cin >> inputcnt;

	prime.insert(2);
	prime.insert(3);
	prime.insert(5);
	prime.insert(7);
	prime.insert(11);
	prime.insert(13);
	prime.insert(17);
	prime.insert(19);

	std::set<unsigned long long> checked;

	for (int i = 0; i < inputcnt; i++) {
		cout << "Case #" << i + 1 << ":" << endl;
		int digitCnt = 0;
		cin >> digitCnt;
		int outputCount = 0;
		cin >> outputCount;

		while (outputCount > 0) {
			unsigned long long divider[11] = {};
			unsigned long long check = makeCheck(digitCnt);
			while (checked.find(check) != checked.end() )
			{
				check = makeCheck(digitCnt);
			}

			bool bCoinAble = true;

			for (int j = 2;j < 11;j++) {
				divider[j] = ChangeDigit(check, j);

				unsigned long long finder = divider[j];
				for (auto p = prime.rbegin(); p != prime.rend();p++) {
					if ((finder % *p) == 0) {
						finder = *p;
						break;
					}
				} // 찾은 프라임 먼저 순회

				if (finder == divider[j] || finder == 1) { // 우선 찾아 놓은 프라임 보다 작은 프라임이 있는지 체크.
					unsigned long long cmp = GetCurMaxPrime();

					while ( cmp < 17 )
					{
						unsigned long long div = 0;
						if (IsPrime(cmp, div)) {
							//prime.insert(cmp);
							if (finder % cmp == 0) {
								finder /= cmp;
								break;
							}
						}

						cmp -= 2; // 짝수는 2빼고 논 프라임
					}

				}

				if (finder == divider[j] || finder == 1) {
					unsigned long long div = 0;
					bool bPrime = IsPrime(finder, div);
					bCoinAble = bCoinAble && !bPrime;
					//if (bPrime) prime.insert(finder);
					if (!bPrime && div != 1) {
						//prime.insert(div);
						divider[j] = div;
					}
				}
				else {
					divider[j] = finder;
					continue;
				}

				if (!bCoinAble) break;
			}

			checked.insert(check);
			if (bCoinAble) {
				cout << check;
				for (int j = 2;j < 11;j++) {
					cout << " " << divider[j];
				}
				cout << endl;
				outputCount--;
			}
			
		}
	}
	fclose(stream);
	fclose(stream2);
    return 0;
}