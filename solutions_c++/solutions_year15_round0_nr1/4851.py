#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;


int main() {

	freopen("A.in","r",stdin);
//	freopen("A.output","W",stdout);
	int T;
	cin>>T;
	int smax;
	int add;
	int count;
	string s;
	int x;
	for (int t = 0; t<T; t++) {
		cout<<"Case #"<<(t+1)<<": ";
		add = 0;
		count = 0;
		cin>>smax;
		cin>>s;
		for (int i=0; i<=smax; i++) {
			x= 	s[i]-48;
			if (i==0) count = x;
			else {
				if (x>0) {
				if (count>=i) {
					count += x;
				} else {
					add += (i-count);
					count += x + add;
				}
				}
//			cout<<"After position "<<i<<" add is "<<add<<endl;
			}
		}
		cout<<add<<endl;
	}
}
