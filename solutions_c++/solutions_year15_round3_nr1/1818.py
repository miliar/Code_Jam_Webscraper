#include <iostream>
#include <cstdio>
using namespace std;
int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int test,r,c,w;
	cin>>test;
	for(int i=1;i<=test;i++){
		cin>>r>>c>>w;
		if(w==1)
			cout<<"Case #"<<i<<": "<<r*c<<endl;
		else if(c%w==0)
			cout<<"Case #"<<i<<": "<<r*((c/w)+w-1)<<endl;
		else
			cout<<"Case #"<<i<<": "<<r*((c/w)+w)<<endl;
	}
	return 0;
}