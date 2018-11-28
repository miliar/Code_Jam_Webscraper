#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
void calc(vector<int>&a, vector<int>&b)
{
	int matches = 0;
	int ans;
	for (int i = 0; i< 4; i++) {
	for (int j = 0; j< 4; j++) {
		if (a[i] == b[j]) {
			matches++;
			ans = a[i];
		}
	}
	}

	if (matches == 0) {
			cout<<"Volunteer cheated!"<<endl;
	} else if (matches == 1) {
			cout<<ans<<endl;
	} else {
			cout<<"Bad magician!"<<endl;
	}
}

int main() {
        fstream f;
	f.open("a.dat",ios::in);
	if (!f.is_open()) {
		throw "Failed to open input";
	}

	int N;
	f>>N;
	for (int i =0 ;i < N; i++) {
		int first, second;
		vector<int> farr;
		vector<int> sarr;

		cout<<"Case #"<<i<<": ";
		f>>first;

		for (int k = 0; k < 4; k++) {
		for (int j = 0; j< 4; j++) {
		     int val;
		     f>>val;
		     if (k == (first-1)) {
		     farr.push_back(val);
		     }
		}
		}

		f>>second;

		for (int k = 0; k < 4; k++) {
		for (int j = 0; j< 4; j++) {
		     int val;
		     f>>val;
		     if (k == (second-1)) {
		     sarr.push_back(val);
		     }
		}
		}

		calc(farr, sarr);

		farr.clear();
		sarr.clear();
	}
        return 0;
}
