#include<iostream>
#include<vector>

using namespace std;


int main(){
	int T;
	int N;
	int cur;
	int tmp;
	int count;
	char c;
	cin >> T;

	for (int i = 0; i < T; i++){
		cin >> N;
		cur = 0;
		count = 0;
		for (int j = 0; j <= N; j++){
			cin >> c;
			tmp = c - '0';
			if (tmp > 0){
				if (cur < j){
					count += j - cur;
					cur = j;
				}
				cur += tmp;
			}
		}
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
	return 0;
}