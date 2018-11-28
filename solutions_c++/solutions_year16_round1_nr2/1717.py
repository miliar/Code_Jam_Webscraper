#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int main() {
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	int TT;
	cin>>TT;
	for (int T=1; T<=TT; ++T) {
		cout<<"Case #"<<T<<":";
		int n;
		cin>>n;
		int count[3000];
		memset(count, 0, sizeof(count));
		for (int i=0; i<2*n-1; ++i)
		  for (int j=0; j<n; ++j) {
		  	int x;
		  	cin>>x;
		  	count[x]++;
		  }
		for (int i=0; i<3000; ++i)
		   if (count[i]%2==1)
		     cout<<" "<<i;
		cout<<endl;
	}
}
