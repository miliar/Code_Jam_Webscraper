#include <iostream>
using namespace std;

int T,k,c,s;

int main() {
	//freopen("D.in","r",stdin);
	//freopen("D.out","w",stdout);
	cin>>T;
	for (int ii=1; ii<=T; ii++) {
		cin>>k>>c>>s;
		cout<<"Case #"<<ii<<": ";
		for (int i=1; i<=s; i++)
			cout<<i<<" ";
		cout<<endl; 
	}
}
