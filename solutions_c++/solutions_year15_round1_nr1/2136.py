#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

int main() {
	//ifstream in("realone");
	ifstream in("A-large.in");
	//ifstream in("A-small-attempt3.in");
	//ifstream in("small");
	int tc_count;
	in >> tc_count;
	for(int i = 0;i<tc_count;++i) {
		int time;
		in >> time;
		int min = 0;
		int max = 0;
		int rate = 0;
		int prev = -1;
		vector<int> mushrooms;	
		for(int j = 0; j<time;++j) {
			int curr;
			in >> curr;
			mushrooms.push_back(curr);
			//cout << curr << endl;
			if(j > 0) {
				//not the first one
				if(curr < prev) {
					//eaten at least some
					min += prev - curr;
				}
				if(prev - curr > rate) rate = prev - curr;
			}
			prev = curr;
		}
		for(int j = 0; j < mushrooms.size() - 1; ++j){
			max += std::min(rate, mushrooms[j]);
		}
		cout << "Case #" << i + 1 << ": " << min << " " << max << endl;

	}
}
