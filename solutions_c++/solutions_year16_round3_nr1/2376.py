#include <iostream>
#include <vector>


using namespace std;

void findTwoMax(const vector<int> &vec, int &fst, int &snd)
{
	int fstValue = 0, sndValue = 0;
	for (int i = 0; i < vec.size(); ++i) {
		if (vec[i] > fstValue) {
			snd = fst;
			sndValue = fstValue;
			fstValue = vec[i];
			fst = i;
		} else if (vec[i] > sndValue) {
			snd = i;
			sndValue = vec[i];
		}
	}
}

int main(int argc, char *argv[])
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int N;
		cin >> N;
		vector<int> vec(N);
		vector<string> plan;
		for (int j = 0; j < N; ++j) {
			cin >> vec[j];
		}

		cout << "Case #" << i << ":";

		while (true) {
			int fst = -1, snd = -1;
			findTwoMax(vec, fst, snd);
			if (fst == -1 && snd == -1) {
				break;
			}

			if (snd == -1) {
				char c = 'A' + fst;
				//cout << " " << c;
				plan.push_back(string(1, c));
				--vec[fst];
			} else if (vec[fst] - 2 >= vec[snd]) {
				char c = 'A' + fst;
				//cout << " " << c << c;
				plan.push_back(string(2, c));
				vec[fst] -= 2;
			} else {
				char f = 'A' + fst, s = 'A' + snd;
				//cout << " " << f << s;
				string str;
				str.push_back(f);
				str.push_back(s);
				plan.push_back(str);
				--vec[fst];
				--vec[snd];
			}
		}

		if (plan[plan.size() - 1].size() == 1) {
			swap(plan[plan.size() - 1], plan[plan.size() - 2]);
		}

		for (auto s : plan) {
			cout << " " << s;
		}
		cout << endl;
	}
	
	return 0;
}

