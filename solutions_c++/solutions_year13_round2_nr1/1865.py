#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

char *bitmap_naive;

long as(long &a, long mote, long *motes, long i) {
	long add = 0;
	if (a == 1) return -1;
	while (a <= mote) {
		// cerr << "Adding " << (a-1) << endl;
		a += (a-1);
		add++;
	}
	return add;
	// for (long j = a - 1; j > 0; j--) {
	// 	// if (j == motes[k]) {
	// 	// 	a -= motes[k];
	// 	// 	k--;
	// 	// }
	// 	if (bitmap_naive[j])
	// 		continue;
	// 	if (a > j) {
	// 		cerr << "Add " << j << endl;
	// 		add++;
	// 		a += j;
	// 		bitmap_naive[j] = 1;
	// 		if (a > mote) return add;
	// 	}
	// }
	// if (add == 0) return -1;
	// return as(a, mote, motes, i);
}

long solve(long a, long m, long *motes) {
	vector<int> sols(m);
	for (int i = 0; i < m; i++)
		sols[i] = 0;
	// int add = 0;
	long i = 0;
	for (i = 0; i < m; i++) {
		// cerr << "Looking at mote " << i << ": " << motes[i] << endl;
		if (a > motes[i]) {
			a += motes[i];
			if (i > 0)
				sols[i] = sols[i-1];
		}
		// else if (i == m - 1) {
		// 	cerr << "Removed the last one" << endl;
		// 	add++;
		// 	sols[i] = add;
		// 	cerr << "sols[" << i << "] = " << sols[i] << endl;
		// } 
		else {
			long num_as = as(a, motes[i], motes, i);
			if (num_as == -1) {
				int add = (i>0)?sols[i-1]:0;
				add += (m-i);
				sols[i] = add;
				break;
			} else {
			// if (num_as > (m-i)) {
			// 	add += (m-i);
			// 	sols[i] = add;
			// 	break;
			// } else {
				int add = (i>0)?sols[i-1]:0;
				add += num_as;
				sols[i] = add;
			}
			a += motes[i];
		}
	}
	int mins = m;
	for (int k = 0; k < min(i+1, m); k++) {
		// cerr << "Sols[" << k << "]=" << sols[k] << endl;
		// cerr << " m - k - 1 = " << (m-k-1) << endl;
		if (sols[k] + (m - k - 1) < mins)
			mins = sols[k] + (m-k-1);
		// cerr << "mins = " << mins << endl;
	}
	return mins;
}

int main(int argc, char **argv) {
	long T;
	cin >> T;
	for (long c = 1; c <= T; c++) {

		long A, M;
		cin >> A;
		cin >> M;
		long * motes = new long[M];
		bitmap_naive = new char[1000010];
		for (int i = 0; i < 1000010; i++)
			bitmap_naive[i] = 0;
		for (long i = 0; i < M; i++) {
			cin >> motes[i];
			bitmap_naive[motes[i]]= 1;
		}
		sort(motes, motes+M);
		// cerr << "Case #" << c << endl;
		// cerr << "My mote: " << A << endl;
		// for (int i = 0; i < M; i++) {
		// 	cerr << " " << motes[i];
		// }
		// cerr << endl;
		long num = solve(A, M, motes);
		cout << "Case #" << c << ": " << num << endl;
		delete []motes;
		delete []bitmap_naive;
	}
	return 0;
}