#include <iostream>
#include <fstream>
using namespace std;
bool test(long long t) {
	if (t%2)
		return false;
	if (t==2)
		return true;
	return test(t/2);
}
int main() {
	//cout<<"Hello World"<<endl;
	//ostream output;
	//output.open("output.txt");
	freopen("output.txt","w",stdout);
	long long p, q ;
	int t,cas;
	cin>>t;
	char tmp;
	int cnt;
	for (cas = 1; cas <= t; cas++) {
		cin>>p>>tmp>>q;
		if (test(q)==false) {
			cout<<"Case #"<<cas<<": impossible"<<endl;
		} else {
			cnt =0;
			while (p<q) {
				cnt++;
				p*=2;
			}
			cout<<"Case #"<<cas<<": "<<cnt<<endl;
		}
	}
	return 0;
}