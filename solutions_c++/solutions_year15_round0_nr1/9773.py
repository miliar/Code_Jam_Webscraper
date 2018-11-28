#include<iostream>
using namespace std;

int main() {
	int t, s;
	cin >> t;
	for(int i = 0; i < t; i++) {
		cin >> s;
		char str[s + 1];
		cin >> str;
		int count_so_far = (int)(str[0] - '0');
		int additional = 0;
		for(int j=1;j<=s; j++) {
			int count = (int)(str[j] - '0');
			if(count > 0 && count_so_far < j) {
				additional += (j - count_so_far);
				count_so_far += additional;
			}
			count_so_far +=count;
		}
		cout << "Case #" << (i + 1) << ": " << additional <<"\n";
	}
}
