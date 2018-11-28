#include <iostream>
using namespace std;
int main()
{
	int n,q;
	cin>>n;
	char c;
	int i=1;
	while(n--) {
		cin>>q;
		int t=0;
		int r=0;
		for(int j=0;j<=q;j++) {
			cin>>c;
			if(t<j) {
				r+=j-t;
				t=j;
			}
			t+=int(c)-'0';
		}

		cout<<"Case #"<<i++<<": ";
		cout<<r<<endl;
	}
}
