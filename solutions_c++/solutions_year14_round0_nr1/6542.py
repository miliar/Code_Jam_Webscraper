#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;


int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int T,tmp,r;
	set<int> ans1,ans2;
	vector<int> ans;
	cin >> T;
	for (int t = 0; t < T; t++){
		ans1.clear();
		ans2.clear();
		ans.clear();
		cin >> r;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++) {
				cin >> tmp;
				if (i==r-1) ans1.insert(tmp);
			}
		}
		cin >> r;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++) {
				cin >> tmp;
				if (i==r-1) ans2.insert(tmp);
			}
		}
		set_intersection(ans1.begin(),ans1.end(),ans2.begin(),ans2.end(),back_inserter(ans));
		cout << "Case #" << t+1 << ": ";
		if (ans.size()==1) cout << *(ans.begin()) << endl;
		else if (ans.size()>1) cout << "Bad magician!" << endl;
		else if (ans.size()<1) cout << "Volunteer cheated!" << endl;
	}
}
