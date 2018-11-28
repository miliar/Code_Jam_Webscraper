#include <iostream>
#include <tuple>
#include <utility>
#include <string>
#include <algorithm>

using namespace std;

int main(){
	int t, n;
	string s;

	cin >> t;

	for (int i = 1; i <= t; i++){
		int j;

		cin >> s;
		int end = s.length(), cnt = 0;

		for (j = end - 1; j >= 0; j--){
			if (s[j] == '-')
				break;
		}

		end = j + 1;

		while (count(s.begin(), s.begin() + end, '-')){
			for (j = 0; j < end; j++){
				if (s[j] == '+')
					break;
			}

			if (j == 0) {
				for (j = 0; j < end; j++){
					if (s[j] == '-')
						break;
				}
				replace(s.begin(), s.begin() + j, '+', '-');
				cnt++;
			}

			for (j = 0; j < end; j++){
				if (s[j] == '+')
					break;
			}

			reverse(s.begin(), s.begin() + end);
			replace(s.begin(), s.begin() + end, '+', '*');
			replace(s.begin(), s.begin() + end, '-', '+');
			replace(s.begin(), s.begin() + end, '*', '-');

			end -= j;
			cnt++;
		}

		cout << "Case #" << i << ": " << cnt << endl;
	}

	return 0;
}

