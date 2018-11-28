#include<iostream>
using namespace std;

int main() {
	freopen("D-small-attempt3.in","r",stdin);
	freopen("Ds.out","w",stdout);
	int T,k=1;
	cin>>T;
	while(T--) {
		int x,r,c;
		bool richard=false;
		cin>>x>>r>>c;
		if(x >=7) {
			richard=true;
		}
		else if((r%x !=0 && c%x!=0) || ((r < x-1) || (c < x-1))) {
			richard=true;
		}
		cout<<"Case #"<<k<<": ";
		if(richard)
			cout<<"RICHARD"<<endl;
		else cout<<"GABRIEL"<<endl;
		k++;
	}
	return 0;
}
