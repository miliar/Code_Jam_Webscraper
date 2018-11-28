#include <iostream>
#include <algorithm>

using namespace std;

int main (int argc, char** argv) {

	int testCases;
	cin >> testCases;

	for (int test = 0; test < testCases; ++test) {

		int N;
		cin >> N;

		int M1 = 0;
		int M2 = 0;

		int mPrev = 0;
		int mRate = 0;

		int* mArray = new int[N];

		for (int n = 0; n < N; ++n) {
			int m;
			cin >> m;

			mArray[n] = m;

			if (n > 0) {
				int mDelta = mPrev - m;
				mRate = std::max(mRate, mDelta);
			}

			if (m < mPrev) {
				M1 += mPrev - m;
			}

			mPrev = m;

		}

		for (int n = 0; n < N - 1; ++n) {
			M2 += std::min(mRate, mArray[n]);
		}

		cout << "Case #" << test + 1 << ": " << M1 << " " << M2 << endl;

	}

	return 0;
}