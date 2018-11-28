#include <iostream>
using namespace std;
#include <stack>
#include <stdio.h>

int getLevel(char ch) {
	if (ch == '+')
		return 0;
	return 1;
}

void timesFlipPancakes(int size) {
	stack <char> pancake;
	char ch;




	for (int i = 0; i < size; ++i)
	{
		int times = 0;
		int count = 1;
		bool group = true;
		bool push = true;



		while ((ch = getchar()) != '\n') {
			//cout << ch << endl;

			if (ch == '+' and push) {
				//cout << "tsaedd+\n";
				pancake.push(ch);
				push = false;
			}
			if (!pancake.empty() and getLevel(pancake.top()) < getLevel(ch)) {
				times++;
				group = true;
				pancake.pop();
				push = true;
				//cout << "tsaedd333\n";
			}
			if (ch == '-' and group) {
				//cout << "tsaedd\n";
				times++;
				group = false;
			}

		}

		// if (times < count and pop) {
		// 	//cout << "a\n";
		// 	times++;
		// }
		//clear stack
		while (!pancake.empty()) {
			pancake.pop();
		}
		// cout << endl;

		cout << "Case #" << i + 1 << ": " << times << endl;
	}


}

int main() {


	int size;

	scanf("%d\n", &size);

	timesFlipPancakes(size);


	return 0;

}