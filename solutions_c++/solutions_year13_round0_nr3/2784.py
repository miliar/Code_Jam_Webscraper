#include <iostream>
//#include <algorithm>
using namespace std;

void bs(){
	int small, big, spos=0, bpos=4;
	int the_num[5] = {1,4,9,121,484};
	cin >> small >> big;
	while (the_num[spos] < small && spos <= 4)
		spos++;
	while (the_num[bpos] > big && bpos >= 0)
		bpos--;
	cout << bpos-spos+1;
}

int main(void){
	int T;
	cin >> T;
	for (int i = 1;i <= T; ++i){
		cout << "Case #" << i << ": ";
		bs();
		cout << endl;
	}
	return 0;
}