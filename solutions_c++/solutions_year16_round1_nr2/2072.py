#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
typedef vector<vector<int> > mat_t;

bool mycompare(vector<int>& left, vector<int>& right) {
	bool isSmall = true;
	for(int i=0;i<left.size(); ++i) {
		if(left[i] > right[i]) {
			isSmall = false;
			break;
		}
	}
	return isSmall;
}

vector<int> find_missing(mat_t& mat) {
	map<int, int> cmap;
	int sz = mat.size()/2 + 1;
	for(int i=0;i<mat.size(); ++i) {
		for(int j=0; j<sz; ++j) {
			int num = mat[i][j];
			cmap[num] += 1;
		}
	}

	map<int, int>::iterator itr = cmap.begin();
	map<int, int>::iterator end = cmap.end();
	vector<int> ans;
	while(itr!=end) {
		//cout<<itr->first<<" ==> "<<itr->second<<endl;
		int num = itr->second;
		int r = num%2;
		if(r != 0) {
			//cout<<"pushing "<<itr->first<<endl;
			ans.push_back(itr->first);
		}
		itr++;
	}

	return ans;
}

int main() {
	int t;
	cin>>t;
	for(int i=1; i<=t; ++i) {
		int n;
		cin>>n;

		mat_t mat;
		int count = 2*n -1;
		int d;
		for(int i=0; i<count; ++i) {
			vector<int> v;
			for(int j=0; j<n; ++j) {
				cin>>d;
				v.push_back(d);
			}

			mat.push_back(v);
		}
		cout<<"Case #"<<i<<": ";
		vector<int> vans = find_missing(mat);
		for(int i=0;i<vans.size(); ++i) {
			cout<<vans[i]<<" ";
		}
		cout<<"\n";

	}
	return 0;
}
