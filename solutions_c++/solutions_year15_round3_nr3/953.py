#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int f(int C, int V, vector<int> &denom)
{
	sort(denom.begin(),denom.end());
	int canGetTo = 0;
	int added = 0;
	int j = 0;
	for (int i = 1; i <= V; i++) {
		if (j < denom.size() && denom[j]==i){
			canGetTo+=denom[j];
			j++;
			continue;
		}
		if (canGetTo < i) {
			canGetTo += i;
			added++;
		}
	}
	return added;
}

int main()
{
	freopen("inC.txt","r",stdin);
	freopen("outC.txt","w",stdout);
	int T;
	cin >> T;
	for (int t= 0; t < T; t++) {
		int C,V,D;
		cin >> C >> D >> V;
		vector<int> denom;
		for (int i = 0; i < D; i++) {
			int x;
			cin >> x;
			denom.push_back(x);
		}
		cout << "Case #" << t+1 << ": " << f(C,V,denom) << endl;
	}
	return 0;
}