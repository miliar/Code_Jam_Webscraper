

#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <sstream>
#include <map>
#include <limits>
#include <cmath>

using namespace std;

int main() {

	int cases;
	cin>>cases;
	for (int i = 1; i<=cases; i++) {
		int ans1;
		cin>>ans1;
		vector<int> histogram(17,0);
		for (int j = 1; j<=4; j++) {
			for (int k = 1; k<=4; k++) {
				int x;
				cin>>x;
				if (j==ans1)
					histogram[x]++;
			}
		}
		int ans2;
		cin>>ans2;
		for (int j = 1; j<=4; j++) {
			for (int k = 1; k<=4; k++) {
				int x;
				cin>>x;
				if (j==ans2)
					histogram[x]++;
			}
		}
		bool found = false;
		int number=-1;
		for (int j = 1; j<histogram.size(); j++) {
			if (histogram[j]==2) {
				if (!found) {
					found = true;
					number=j;
				}
				else {//found twice
					number=-1;
					break;
				}
			}

		}

		if(found&&number!=-1)
		cout<<"Case #"<<i<<":"<<" "<<number<<endl;
		else if(found)
			cout<<"Case #"<<i<<":"<<" "<<"Bad magician!"<<endl;
		else
			cout<<"Case #"<<i<<":"<<" "<<"Volunteer cheated!"<<endl;
	}
	return 0;
}

