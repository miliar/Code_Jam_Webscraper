#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");

	int caseCount;
	cin >> caseCount;

	caseCount++;
	for (int casei = 1; casei < caseCount; casei++) {
		int arr[1000];

		int D;
		cin >> D;

		int maxx = 0;
		for (int i = 0; i < D; i++) {
			cin >> arr[i];
			maxx = max(maxx, arr[i]);
		}

		int minn = maxx;
        maxx++;
		for (int i = 1; i < maxx; i++) {
            int sum = i;
            for (int j = 0; j < D; j++) {
				int curr = arr[j];
                if (curr > i) {
                    if (curr % i == 0) {
                        sum += curr / i - 1;
                    } else {
                        sum += curr / i;
                    }
                }
            }

            minn = min(minn, sum);
        }


		cout << "Case #" << casei << ": " << minn << endl;
	}

	return 0 ;
}
