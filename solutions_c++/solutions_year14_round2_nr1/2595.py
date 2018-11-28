#include <iostream>
#include <vector>
#include <limits>
#include <iomanip>

using namespace std;

void outcase(int i) {
	cout<<"Case #"<<i<<": ";
}

int main() {
	cin.sync_with_stdio(false);

	int T; cin>>T;

	for(int t = 1; t <= T; t++) {
		int N; cin>>N;

		vector<string> S(N);
		for(int i = 0; i < N; i++)
			cin>>S[i];

		vector<string> SS(N);
		vector<vector<int> > A(N);

		for(int i = 0; i < N; i++) {
			for(int j = 0; j < S[i].size();) {
				SS[i].push_back(S[i][j]);
				int c = 0; j++;
				while(j < S[i].size() && S[i][j] == SS[i].back()) {j++;c++;}
				A[i].push_back(c+1);
			}
		}

		int i;
		for(i = 0; i < N-1; i++)
			if(SS[i] != SS[i+1])
				break;

		if(i < N-1) {
			outcase(t); cout<<"Fegla Won"<<endl;
			continue;
		}

		int count = 0;
		for(int i = 0; i < SS[0].size(); i++) {
			int best = 1000000;
			for(int j = 1; j <= 200; j++) {
				int curr = 0;
				for(int h = 0; h < N; h++)
					curr += abs(A[h][i]-j);
				if(curr < best) best = curr;
			}
			count += best;
		}

		outcase(t); cout<<count<<endl;
	}

	return 0;
}
