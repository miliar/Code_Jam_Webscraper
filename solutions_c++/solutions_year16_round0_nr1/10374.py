#include <iostream> 
using namespace std; 

int caseT() {
	int N, newnum, base, i;
	cin >> N;
	bool A[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	i = 1;
	newnum, base = N;

	if (N == 0) {
		return -1;
	}
	else {
		while (true) {
			newnum = base;
			while (newnum > 0) {
				A[newnum%10] = true;
				if ((A[0] && A[1] && A[2] && A[3] && A[4] && A[5] 
					&& A[6] && 
					A[7] && A[8] && A[9])) { 
					return base;
				}
				newnum = (newnum - newnum%10)/10;
			}
			i++;
			base = i*N;
		}
	}

	return 0;
}


int main() {
	int T;
	int ans;
	cin >> T;
	for (int j = 0; j < T; j++){
		ans = caseT();
		if (ans == -1) {
			cout << "Case #" << j+1 << ": " << "INSOMNIA" << endl;
		}
		else
			cout << "Case #" << j+1 << ": " << ans << endl;
	}
	return 0;
}