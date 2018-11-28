#include <iostream>
#include <algorithm>

using namespace std;

string s;

int main() {
	int n;
	cin>>n;
	int count;
	int req;
	int temp;
	int waste;
	for(int i=0;i<n;i++) {
		count=0;
		req=0;
		temp=0;
		cin>>waste;
		cin>>s;
		for(int j=0;j<s.size();j++) {
			temp=s[j]-48;
			if(j<=count||temp==0) {
				count+=temp;
			}
			else {
				req =req + j-count;
				count+=temp+j-count;
			}
		}
		cout<<"Case #"<<i+1<<": "<<req<<endl;
	}
}