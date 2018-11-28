#include <iostream>
#include <set>
using namespace std;

int main() {
	int cases;
	cin>>cases;

	int casenum=1;

	while(cases--) {
		int num;
		cin >> num;

		if(num==0) {
			cout << "Case #" << casenum++ << ": INSOMNIA" << endl;
			continue;
		}

		set<int> seen;
		int count=1;
		while(seen.size()!=10) {

			int test = num*count;

			while(test!=0) {
				seen.insert(test%10);
				test /= 10;
			}
			count++;
		}

		cout << "Case #" << casenum++ << ": " << num*(count-1) << endl;

	}
}