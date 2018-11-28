#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

/*void print_myset(set<int> &myset) {
	cout<<"\nPrinting all the elems: ";
	for(set<int>::iterator i=myset.begin(); i != myset.end(); i++) {
		cout<<*i<<" ";
	}
	cout<<endl;
}*/


int main() {
	int T, d;
	long int N, tmp, count, curr_num;
	set<int> myset;
	cin>>T;

	for(int i=1; i<=T; i++) {
		myset.clear();
		tmp = count = 0;
		cin>>N;
		cout<<"Case #"<<i<<": ";

		if(0 == N) {
			cout<<"INSOMNIA\n";	continue;
		}
		
		while(true) {
			if(0 == tmp) {
				curr_num = tmp = N * ++count;
				//cout<<"\ncount="<<count<<" curr_num="<<curr_num<<endl;
			}
			d = tmp%10;
			tmp /= 10;
			if(myset.end() != myset.find(d)) {
				continue;
			}
			myset.insert(d);
			if(10 == myset.size()){
				cout<<curr_num<<endl;
				break;
			}
		}
		//print_myset(myset);
	}
	return 0;
}