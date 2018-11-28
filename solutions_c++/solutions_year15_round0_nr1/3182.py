#include<iostream>
#include<string>
using namespace std;

int main() {
	int t; cin>>t;
	for (int c=1; c<=t; c++) {
		int smax; cin>>smax;
		char cur;
		int ret=0, tot=0;
		for (int i=0; i<smax+1; i++) {
			cin>>cur;
			int tmp=cur-'0';
			if(tot<i) {
				int add=i-tot;
				tot+=add, ret+=add;
			}
			tot+=tmp;
		}
		cout << "Case #" << c << ": " << ret << endl;
	}
	return 0;
}
