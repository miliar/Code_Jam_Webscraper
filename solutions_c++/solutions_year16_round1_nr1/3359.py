#include <iostream>
#include <deque>
#include <string>
#include <cstdlib>
using namespace std;

int main(void) {
	int nbTests;
	scanf("%d", &nbTests);
	for (int iTest = 1; iTest <= nbTests; iTest++) {
		string s;
		cin >> s;
		deque<char> res;
		res.push_back(s[0]);
		for (int iCar = 1; iCar < s.length(); iCar++) {
			if (s[iCar] >= res[0])
				res.push_front(s[iCar]);
			else
				res.push_back(s[iCar]);
		}
		printf("Case #%d: ", iTest);
		for (int i = 0; i < res.size(); i++)
			printf("%c", res[i]);
		printf("\n");
	}
	return 0;
}
