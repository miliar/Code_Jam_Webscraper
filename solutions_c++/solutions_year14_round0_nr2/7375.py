#include <iostream>
#include <cmath>
using namespace std;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int z;
	cin>>z;
	for(int k=1;k<=z;++k){
		double c,f,x,v=2,t=0;
		cin>>c>>f>>x;
		double a=x/v;
		double b=c/v+x/(v+f);
		while(b<a&&x>0){
			t+=c/v;
			v+=f;
			a=x/v;
			b=c/v+x/(v+f);
		}
		t+=x/v;
		cout<<"Case #"<<k<<": ";
		printf("%.07lf",t);
		cout<<endl;
	}
	return 0;
}