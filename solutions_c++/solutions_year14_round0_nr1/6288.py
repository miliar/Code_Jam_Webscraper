#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;



int main() {
	int T;
	cin>>T;
	for(int cases = 1; cases<=T; cases++) {
		vector<int> v1(16), v2(16);
		vector<int> p1(4), p2(4);
		int row1, row2;
		cin>>row1;
		row1--;
		for_each(begin(v1), end(v1), [](int& i){cin>>i;});
		copy(begin(v1)+row1*4, begin(v1)+(row1+1)*4, begin(p1));
		
		
		cin>>row2;
		row2--;
		for_each(begin(v2), end(v2), [](int& i){cin>>i;});
		copy(begin(v2)+row2*4, begin(v2)+(row2+1)*4, begin(p2));
		
		cout<<"Case #"<<cases<<": ";
		auto r1 = find_first_of(begin(p1), end(p1), begin(p2), end(p2));
		int d1 = distance(begin(p1), r1);
		reverse(begin(p1), end(p1));
		auto r2 = find_first_of(begin(p1), end(p1), begin(p2), end(p2));
		int d2 = 3-distance(begin(p1), r2);
		if(r1==end(p1)) {
			cout<<"Volunteer cheated!";
		}
		else
		if(d1!=d2) {
			cout<<"Bad Magician!";
		}
		else {
			//r1 ruined by reverse
			cout<<*r2;
		}
		cout<<'\n';
	}
	
}
