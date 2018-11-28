#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solve(vector<int> m, int beg, int las, int cur) {
	if (las - beg < 1) return 0;
	int nex = m.at(beg);
	if (cur > nex){
		return solve(m, beg+1, las, cur+nex);
	} else {
		int m2 = solve(m, beg+1, las, cur);
		int m1; 
		if (cur != 1) m1 = solve(m, beg, las, 2*cur-1);
		else return 1+ m2;
		return 1+min(m1,m2);
	}
}

int main() {
	int T, index;
	cin >> T;
	for (index = 1; index<=T; index++) 
	{
		cout << "Case #" << index << ": ";
		int mote, num;
		cin >> mote >> num;
		vector<int> motes;
		int temp;
		for (int i=0; i<num; i++){
			cin >> temp;
			motes.push_back(temp);
		}
		sort(motes.begin(), motes.end());
		int result = solve(motes, 0, num, mote);
		cout << result << endl;
	}
	return 0;
}
