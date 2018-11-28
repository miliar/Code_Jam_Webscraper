#include <iostream>

using namespace std;

int main(){
	freopen("D:\\Downloads\\A-large.in", "r", stdin); freopen("D:\\Downloads\\A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++){
		int sm;
		cin >> sm;
		int add = 0;
		for (int i = 0, crowd = 0; i <= sm; i++){
			add += max(i-crowd, 0);
			crowd = max(crowd, i);
			char c;
			cin >> c;
			c -= '0';
			crowd += c;
		}
		cout << "Case #" << t+1 << ": " << add << endl;
		//system("pause");
	}
	return 0;
}
