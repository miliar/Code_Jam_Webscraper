#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int main() {

    int TC;
    cin >> TC;

    for (int tc = 1; tc <= TC; tc++) {
	string input;
	string result;
	cin >> input;

	int len = (int)input.size();
	result += input[0];
	for (int i = 1; i < len; i++) {
	    string tmp1, tmp2;
	    tmp1 = input[i] + result;
	    tmp2 = result + input[i];

	    int tmp_len = (int)tmp1.size();
	    int choice = 1;
	    for (int j = 0; j < tmp_len; j++) {
		if (tmp1[j] == tmp2[j]) continue;
		if (tmp2[j] > tmp1[j]){
		    choice = 2;
		}
		break;
	    }

	    if (choice == 1) result = tmp1;
	    else result = tmp2;
	}

	printf("Case #%d: %s\n", tc, result.c_str());
    }
    return 0;
}
