#include <cstdio>
//#include <list>
//using namespace std;

int main(void) {
	int testCase;
	int number, tempNumber, temp;
	int checkDigitsSum = 0;
	int count = 1;
	//list<int> listResult;

	scanf_s("%d", &testCase);

	for (int i = 0; i < testCase; i++) {
		scanf_s("%d", &number);

		count = 1;
		int checkDigits[10] = { 0 };

		while (1) {
			tempNumber = number * count;
			temp = tempNumber;
			while (1) { // 자리수 검사
				checkDigits[tempNumber % 10] = 1;
				tempNumber = tempNumber / 10;
				if (tempNumber == 0) break;
			}

			checkDigitsSum = 0;
			for (int j = 0; j < 10; j++) {
				checkDigitsSum += checkDigits[j];
			}

			if (checkDigitsSum == 10) {
				printf("Case #%d: %d\n", i + 1, temp);
				//listResult.push_back(temp);
				break;
			}
			count++;

			if (count > 1000000) {
				printf("Case #%d: INSOMNIA\n", i + 1);
				//listResult.push_back(-1);
				break;
			}
		}
	}/*
	int x = 0;
	while (listResult.size() != 0) {
		x++;
		if (listResult.front() == -1) printf("Case #%d: INSOMNIA\n", x);
		else printf("Case #%d: %d\n", x, listResult.front());
		listResult.pop_front();
	}*/

	return 0;
}