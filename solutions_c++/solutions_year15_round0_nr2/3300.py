#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool comp(int i,int j) { return (i>j); }


int calc(vector<int> v, int a) {
 
 int sum = a;

 for(int i=0; i<v.size(); i++)
 	sum += (v[i]-1)/a;

return sum;
}

int main() {
	
	int cases;
	cin >> cases;

	int c=1;

	while(cases--) {

	int n;
	cin >> n;

	vector<int> pancake;

	for(int i=0; i<n; i++) {
		int e;
		cin>>e;
		pancake.push_back(e);
	}



	int maximum=10000;

	int ans = maximum;

	for(int i=1; i<=maximum; i++) {
		ans = min(ans, calc(pancake, i));
	}

	

	cout << "Case #" << c++ << ": " << ans << endl;

	}
	return 0;
}