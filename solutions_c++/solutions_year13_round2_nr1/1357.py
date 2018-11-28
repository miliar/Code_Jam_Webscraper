#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <climits>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int tt=1; tt<=T; tt++) {
		int A, N;
		vector<int>  motes;
		cin >> A >> N;

		for (int i=0; i<N; i++) {
			int mote;
			cin >> mote;
			motes.push_back(mote);
		}

		if (A <= 1) {
			cout << "Case #" << tt << ": " << N << endl;
			continue;
		}

		sort(motes.begin(),motes.end());

		//sort(motes.begin(),motes.end());
		//cout << motes.size() << endl;
		stack<pair<int, pair<vector<int>, int> > > dfs;
		dfs.push(make_pair(A, make_pair(vector<int>(motes), 0)));
		int minops = INT_MAX;

		while(dfs.size() > 0) {

			pair<int, pair<vector<int>, int> > item = dfs.top();
			dfs.pop();

			int current_mote = item.first;
			vector<int> motevector = item.second.first;
			int operations = item.second.second;

			if (motevector.size() == 0) {
				minops = min(minops,operations);
			}

			if (operations >= minops)
				continue;

			int next_mote = *(motevector.begin());
			motevector.erase(motevector.begin());

			if (current_mote > next_mote) {
				current_mote += next_mote;
				dfs.push(make_pair(current_mote,make_pair(motevector,operations)));
			} else {
				operations++;

				dfs.push(make_pair(current_mote,make_pair(motevector,operations)));

				motevector.insert(motevector.begin(), next_mote);
				motevector.insert(motevector.begin(), current_mote-1);
				dfs.push(make_pair(current_mote,make_pair(motevector,operations)));		
			}


			//int mote = motes.top();
			//motes.pop();
			////cout << "mote :" << mote << endl;
			//if (current > mote) {
			//	current += mote;
			//} else {
			//	if ((2*current-1) > mote)
			//		current = (2*current)-1+mote;
//
			//	operations++;
			//}
		}

		cout << "Case #" << tt << ": " << minops << endl; 
	}
}