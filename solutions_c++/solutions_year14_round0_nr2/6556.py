#include <iostream>

using namespace std;

int main() {

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int t,l;
	long double i,c,f,x,ans,time1,time2,base=0;
	
	cin>>t;

	for(l=0;l<t;++l) {

		cin>>c>>f>>x;
		
		i=2;
		time1=x/i;
		base=(c/i);
		i+=f;
		time2=base+x/i;

		while (time2<time1) {
			time1=time2;
			base+=(c/i);
			i+=f;
			time2=base+x/i;
		}
		
		cout.precision(10);
		cout<<"Case	#"<<l+1<<": "<<min(time1,time2)<<endl;
	}

	return 0;
}