#include <iostream>
#include <set>
using namespace std;
int main() {
	int T;
	cin>>T;
	for(int i = 1; i<= T; ++i) {
		int number;
		cin>>number;
		if(number == 0) {
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		}else {
			set<int> c;
			int sum = 0;
			while(c.size() != 10) {
				sum = sum + number;
				int tmp = sum;
				while(tmp>0){
					c.insert(tmp%10);
					tmp = tmp/10;
				}
			}
			cout<<"Case #"<<i<<": "<<sum<<endl;
		}

	}
}
