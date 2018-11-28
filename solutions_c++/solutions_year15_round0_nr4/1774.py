#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int testNum;
	cin >> testNum;
	int caseNum = 0;
	while (++caseNum <= testNum) {
		int X, R, C;
		cin >> X >> R >> C;
		bool ret;
		switch (X) {
			case 1: ret = true; break;
			case 2: ret = ((R*C) % 2 == 0); break;
			case 3: if ((R*C)%3 != 0)
						ret = false;
					else {
						if (R*C == 3)
							ret = false;
						else ret = true;
					}
					break;
			case 4: if ((R*C)%4 != 0)
						ret = false;
					else {
						if (R*C < 12)
							ret = false;
						else ret = true;
					}
					break;
		}
		if(ret)
			printf("Case #%d: GABRIEL\n",caseNum);
		else
			printf("Case #%d: RICHARD\n",caseNum);
	}
	return 0;
}
