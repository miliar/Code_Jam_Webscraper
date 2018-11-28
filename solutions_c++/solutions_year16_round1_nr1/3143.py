#include <bits/stdc++.h>

using namespace std;

deque <char> d;

int main(void){
	string str;
	int i, j, t;

	ios::sync_with_stdio(false);

	cin >> t;

	for (i = 0; i < t; i++){
		cin >> str;

		d.push_back(str[0]);

		for (j = 1; j < str.size(); j++){
			if (str[j] >= d.back()){
				d.push_back(str[j]);
			}
			else{
				d.push_front(str[j]);
			}
		}

		cout << "Case #" << i + 1 << ": ";
		while (!d.empty()){
			cout << d.back();
			d.pop_back();
		}
		cout << endl;
	}

	return 0;
}