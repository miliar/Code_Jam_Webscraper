#include "iostream"
#include "cmath"
using namespace std;

int sleepat(int start) {
	if(start == 0) return -1;
	bool checknum[10];
	for(int i=0; i<10; ++i)
	    checknum[i] = false;
	int count = 0;
	int A = start;
	while(count < 10) {
		int times = log10(A)+1;
		int inner = A;
		while(times > 0) {
			if(!checknum[inner%10]) {
				checknum[inner%10] = true;
				count++;
				if(count == 10) return A;
			}
			inner /= 10;
			times--;
		}
		A += start;
	}
	return A;
}

int main() {
	int T;
	cin >> T;
	int ans[T];
	for(int i=0; i<T; ++i) {
	    int N;
	    cin >> N;
	    ans[i] = sleepat(N);
	}
	for(int i=0; i<T; ++i) {
	    if(ans[i] == -1)
		    cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
		else
			cout << "Case #" << i+1 << ": " << ans[i] << endl;
	}
	// End of Program //
		return 0;
}