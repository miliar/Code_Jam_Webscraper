#include <iostream>
#include <set>
using namespace std;
int main() {
	int T;
	cin>>T;
	for(int i = 1; i<= T; ++i) {
		string tmp;
		cin>>tmp;
		int number = 0;
		bool beg = false;
		for(int i = 0; i < tmp.length()-1; ++i) {
			if(tmp[i] != tmp[i+1]) {
				number++;
			}
		}
		if(tmp[tmp.length()-1] == '-') {
			number++;
		}
		cout<<"Case #"<<i<<": "<<number<<endl;
		/*
		if(number == 0) {
			
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
		}*/

	}
}
