#include <iostream>
#include <queue>
#include <string>
using namespace std;

#define DBG(x) cout<<#x<<" = "<<x<<"\n";

int main()
{
	int t;
	long long i,r,f,prvy,pocet;
	cin>>t;
	for(i=0;i<t;i++){
		cin>>r>>f;
		pocet=0;
		prvy=2*r+1;
		do{
			pocet++;
			f-=prvy;
			prvy+=4;
		}
		while(f-prvy>=0);
		cout<<"Case #"<<i+1<<": "<<pocet<<"\n";

	}
	return 0;
}
