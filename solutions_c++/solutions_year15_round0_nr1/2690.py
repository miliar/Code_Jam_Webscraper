#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	int total = T;
	while(T>0) {
		T--;
		int n;
		cin >> n;

		//int num;
		//cin >> num;
		//std::vector<int> v;
		int count = 0;
		int newM = 0;
		for (int i = 0; i < n+1; ++i)
		{
			char c;
			cin >> c;
			int tmp = c - '0';
			//cout << tmp << endl;
			if(count >= i) {
				count+=tmp;
			}
			else if(tmp > 0) {
				newM += i-count;
				count = i + tmp;
			}
			//n = n/10;
		}
		cout << "Case #" << total-T << ": " << newM << endl;
	}
}