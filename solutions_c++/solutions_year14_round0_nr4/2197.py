#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

void solve(vector <double> P1, vector <double> P2) {
    int ans1=0, ans2=0, n=P1.size();
	vector <double> PP1, PP2;
	PP1=P1;PP2=P2;
	sort(PP1.begin(), PP1.end());
	sort(PP2.begin(), PP2.end());
		
	// normal:
	for (int i=0; i<n; i++)
		if (PP1.back() > PP2.back()) {
			PP1.pop_back();
			PP2.erase(PP2.begin());
			ans2++;
		}
		else {
			PP1.pop_back();
			PP2.pop_back();
		}
	
	// deceitful:
	sort(P1.begin(), P1.end());
	sort(P2.begin(), P2.end());
	for (int i=0; i<n; i++)
		if (P1.front() < P2.front()) {
			P1.erase(P1.begin());
			P2.pop_back();
		}
		else {
			P1.erase(P1.begin());
			P2.erase(P2.begin());
			ans1++;
		}
	cout << ans1 << " " << ans2;
}

int main() {
//    freopen("D-small-attempt0.in", "rt", stdin);
//    freopen("D-small.out", "wt", stdout);
    freopen("D-large.in", "rt", stdin);
    freopen("D-large.out", "wt", stdout);
   
    int T;
    cin>>T;

    for (int i=1; i<=T; i++) {
        int N;cin>>N;
		double n1, n2;
		vector <double> P1, P2;
        for (int j=0; j<N; j++) {
			cin>>n1;
			P1.push_back(n1);
		}
        for (int j=0; j<N; j++) {
			cin>>n2;
			P2.push_back(n2);
		}
        cout << "Case #" << i << ": ";
		solve(P1,P2);
		cout << endl;
    }
}