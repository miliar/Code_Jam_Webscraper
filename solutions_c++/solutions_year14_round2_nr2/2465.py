#include<iostream>
using namespace std;
int main() {
	int t,a,b,k,count=0;
	cin>>t;
	int l=1;
	while(t--) {
		cin>>a>>b>>k;
		for(int i=0;i<a;i++) {
			for(int j=0;j<b;j++) {
				int x=i&j;
				//cout<<"x="<<x<<endl;
				if(x < k)
					count++;
			}
		}
		cout<<"Case #"<<l<<": "<<count<<endl;
		count=0;
		l++;
	}
	return 0;
}
