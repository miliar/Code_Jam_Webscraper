#include <iostream>

using namespace std;
	
int a[100];

int main() {
	int N;
	cin >> N;
	for (int test = 1; test <= N; test ++) {
		cout << "Case #" << test << ": ";
		int sum = 0;
		string s;
		cin >> s;
		int n = (int)s.size();
		for(int i=0; i<n; i++)
			a[i] = s[i] == '+' ? 1 : 0;
		for(int i=n-1; i>=0; --i) {
			if (a[i] == 0) {
				for(int j=0; j<=i; j++)
					a[j] = 1 - a[j];
				sum ++;
			}
		}
		cout << sum << endl;

	}
	
}
