#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<math.h>

using namespace std;

bool solve(long& A, long add, vector<long> motes);

int main() {

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T, N;
	long A;

	cin >> T;
	for (int i = 0; i < T; i++) {
		vector<long> motes;
		cin >> A >> N;


		for (int j = 0; j < N; j++) {
			long mote;
			cin >> mote;
			motes.push_back(mote);
		}

		if (A == 1) {
			cout << "Case #" << i+1 << ": " << N << endl;
			continue;
		}
		
		std::sort(motes.begin(), motes.end());

		long count = 0;		
		while (motes.size() > 0) {
			long smallestSize = *motes.begin();
			if (A > smallestSize) {
				A += smallestSize;
				motes.erase(motes.begin());
			} else {
				if (motes.size() == 1) {
					motes.pop_back();
					count++;	
				} else {
					bool pass = true;
					long add = 1, tmpA = A;
					vector<long> tmp(motes.begin(), motes.begin()+1);
					while (!solve(tmpA, add, tmp)) {
						add++;
						tmpA = A;
						tmp.clear();
						if (motes.begin() + add != motes.end()) {
							tmp.assign(motes.begin(), motes.begin() + add);
						} else {
							pass = false;
							break;
						}
					}
					if (pass) {
						count += add;
						for (int j = 0; j < add; j++)
							motes.erase(motes.begin());
						A = tmpA;
					} else {
						count += motes.size();
						motes.clear();						
					}
				}
			}
		}

		cout << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}

bool solve(long& A, long add, vector<long> motes)
{
	for (long i = 0; i < add; i++) {
		A += A - 1;
		while (motes.size()>0) {
			if (A > *motes.begin()) {
				A += *motes.begin();
				motes.erase(motes.begin());
			} else
				break;
		}
	}
	if (motes.size() == 0)
		return true;
	else
		return false;
}