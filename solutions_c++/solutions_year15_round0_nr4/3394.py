#include <iostream>
#include <string>
#include <algorithm>
#include <utility>

using namespace std;

int xs[100];
int rs[100];
int cs[100];

bool richard_win[100];

int main(){
	//input
	int test_case_no;
	cin >> test_case_no;
	for (int i = 0; i < test_case_no; i++){
		cin >> xs[i] >> rs[i] >> cs[i];
	}

	//calculate
	for (int i = 0; i < test_case_no; i++){
		if (((rs[i] * cs[i]) % xs[i]) != 0){
			richard_win[i] = true;
			continue;
		}

		if (xs[i] == 1){
			richard_win[i] = false;
			continue;
		}

		if (xs[i] == 3){
			if ((cs[i] < 2) || (rs[i] < 2)){
				richard_win[i] = true;
			}
			continue;
		}

		if (xs[i] == 4){
			if ((cs[i] < 2) || (rs[i] < 2) || (rs[i] == 2) || (cs[i] == 2)){

				richard_win[i] = true;
			}
			continue;
		}
	}

	//output
	for (int i = 0; i < test_case_no; i++){
		cout << "Case #" << i + 1 << ": ";
		if (richard_win[i]){
			cout << "RICHARD" << endl;
		}
		else {
			cout << "GABRIEL" << endl;
		}
	}

}