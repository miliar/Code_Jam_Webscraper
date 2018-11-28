#include <string>
#include <iostream>
#include <list>
using namespace std;

int main(void) {
	int testCase, count;
	list<char> listStack, tempStack;
	string x;

	cin >> testCase;
	for (int i = 0; i < testCase; i++) {
		cin >> x;
		count = 0;
		for (int j = 0; j < x.size(); j++) { // 입력 스트링을 list로
			listStack.push_back(x[j]);
		}

		while (1) {
			while (listStack.back() == '+') {
				listStack.pop_back();
				if (listStack.size() == 0) {
					break;
				}
			}

			if (listStack.size() == 0) {
				break;
			}

			if (listStack.front() == '-') { // 처음 - 끝 -
				while (listStack.size() != 0) {
					if (listStack.front() == '+') {
						tempStack.push_front('-');
						listStack.pop_front();
					}
					else {
						tempStack.push_front('+');
						listStack.pop_front();
					}
				}
				listStack = tempStack;
				tempStack.clear();
			}
			else { // 처음 + 끝 -
				while (listStack.front() != '-') {
					tempStack.push_front('-');
					listStack.pop_front();
				}
				while (tempStack.size() != 0) {
					listStack.push_front('-');
					tempStack.pop_front();
				}
			}

			count++;
		}
		listStack.clear();

		cout << "Case #"<<i+1<<": "<<count<<endl;
	}

	return 0;
}