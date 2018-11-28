#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) { 
		cout<<"Case #"<<i<<":";
		int k,c,s;
		cin>>k>>c>>s;
		for(int j=1;j<=k;j++) { 
			cout<<" "<<j;
		}
		cout<<endl;
	}
	return 0;
}

