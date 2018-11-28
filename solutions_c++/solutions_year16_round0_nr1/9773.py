#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int testcase;
	cin >> testcase;

	for (int T = 0; T < testcase; T++) {
		int N;
		cin >> N;
		int j = 1;
		int visit[111111] = { 0 };
		int num = N;
		int arr[11] = { 0 };
		int finish = 0;
		while (finish==0) {
			visit[num] = 1;
			
			int tmp = num;
			int i = 1;
			while (tmp > 0) {
				int a = (tmp / pow(10, i));
				int b = a * pow(10, i);
				int c = tmp - b;
				arr[c] = 1;
				tmp /= 10;
			}


			int f = 0;
			for (int i = 0; i < 10; i++) {
				if (arr[i] == 1) {
					f++;
				}
			}
			if (f == 10) {
				finish = 1;
				break;
			}

			j++;
			num = j*N;
			if (visit[num] == 1) {
				num = (j - 1)*N;
				break;
			}
		}
		if (finish == 1) {
			cout << "Case #" << T + 1 << ": " << num << endl;
		}
		else {
			cout << "Case #" << T + 1 << ": " << "INSOMNIA" << endl;
		}


	}
	return 0;	// 정상종료 시 반드시 0을 리턴해야 합니다.
}