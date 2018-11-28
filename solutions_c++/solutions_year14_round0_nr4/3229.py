#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int T, n, ans1, ans2;
	double naomi[1300], ken[1300];
	cin >> T;

	for (int i1 = 1; i1 <= T; i1++){
		cin >> n;
		ans1 = ans2 = 0;
		for (int i = 0; i < n; i++){cin >> naomi[i];}
		for (int i = 0; i < n; i++){cin >> ken[i];}
		sort(naomi, naomi + n);
		sort(ken, ken + n);

		int head = 0, tail = n-1;
		for (int i = 0; i < n; i++){
			if (naomi[i] < ken[head]){tail--;}
			else {
				head++;
				ans1++;
			}
		}
		int j = 0;
		for (int i = 0; i < n; i++){
			while (naomi[i] > ken[j] && j < n-1){j++;}
			if (naomi[i] < ken[j] && j < n){
				ans2++;
				j++;
			}
			else if (j < i){j++;}
		}
		ans2 = n-ans2;

		cout << "Case #" << i1 << ": " << ans1 << ' ' << ans2 << endl;
	}
	return 0;
}