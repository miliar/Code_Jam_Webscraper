#include <iostream>
#include <vector>
#include <string>
using namespace std;

int T;
int N;
vector<int> vals;

bool majority(int a, int total) {
	return 2*a > total;
}

int main()
{
	cin >> T;
	int nt =1;
	while(nt <= T) {
		cin >> N;
		vals.assign(N, 0);
		int total = 0;
		for (int i = 0; i < N; ++i)
		{
			cin >> vals[i];
			//cout << vals[i] << endl;
			total += vals[i];
		}

		vector<int> selected(N, 0);
		string s1;
		string s2;
		cout << "Case #" << nt << ":";

		while(total > 0){
			int idx1 = -1;
			int idx2 = -1;
			int idx3 = -1;

			int current_max = 0;
			for (int i = 0; i < N; ++i) {
				if (selected[i] == 0 && vals[i] > current_max) {
					current_max = vals[i];
					idx1 = i;
				}
			}
			if (idx1 >= 0 && idx1 < N)
				selected[idx1] = 1;

			current_max = 0;
			for (int i = 0; i < N; ++i) {
				if (selected[i] == 0 && vals[i] > current_max) {
					current_max = vals[i];
					idx2 = i;
				}
			}
			if (idx2 >= 0 && idx2 < N)
				selected[idx2] = 1;

			current_max = 0;
			for (int i = 0; i < N; ++i) {
				if (selected[i] == 0 && vals[i] > current_max) {
					current_max = vals[i];
					idx3 = i;
				}
			}
			if (idx3 >= 0 && idx3 < N)
				selected[idx3] = 1;

			if (idx1>=0)
				selected[idx1] = 0;			
			if (idx2>=0)
				selected[idx2] = 0;			
			if (idx3>=0)
				selected[idx3] = 0;			

			// verify two max
			bool take2 = true;
			//cout << "take2" << endl;
			if (idx1>=0 && idx2>=0 && vals[idx1] > 0 && vals[idx2] > 0) {
				if (idx1 >=0 && majority(vals[idx1]-1, total-2) ) {
					take2 = false;
				}
				if (idx2 >=0 && majority(vals[idx2]-1, total-2) ) {
					take2 = false;	
				}
				if (idx3 >=0 && majority(vals[idx3], total-2) ) {
					take2 = false;	
				}
			} else {
				take2 = false;
			}
			//cout << "take2" << endl;

			if (take2) {
				vals[idx1] = vals[idx1] - 1;
				vals[idx2] = vals[idx2] - 1;
				s1 = 'A'+idx1;
				s2 = 'A'+idx2;
				cout << " " << s1 << s2;
				total -= 2;
			} else {
				vals[idx1] = vals[idx1] - 1;
				s1 = 'A'+idx1;
				cout << " " << s1;
				total--;
			}

		}

		cout << endl;

		nt++;
	}
	return 0;
}