#include <iostream>
#include <iomanip>
using namespace std;

long double c,f,x;
unsigned long long pnum,pden;
int ans;


unsigned long long gcd(unsigned long long a,unsigned long long b) {
	if(a>b) return gcd(b,a);
	if(a==0) return b;
	return gcd(b%a,a);
}

void cadd(int idx) {
	pnum=pnum*(2+idx*f)+pden;
	pden=pden*(2+idx*f);
	unsigned long long g=gcd(pnum,pden);
	pnum/=g;
	pden/=g;
}

int main() {
	int t;
	cin>>t;
	for(int tc=1;tc<=t;++tc) {
		cin>>c>>f>>x;
		if(c>=x) cout<<"Case #"<<tc<<": "<<setprecision(10)<<x/2<<"\n";
		else {
			for(int i=0;;++i) {
				if(x/(2.0+(i+1)*f)>(x-c)/(2.0+i*f)) {
					ans=i;
					break;
				}
			}
			pnum=0,pden=1;
			long double pval=0;
			for(int i=0;i<ans;++i) {
				pval+=(c/(2.0+i*f));
			}
			pval+=x/(2.0+ans*f);
			cout<<"Case #"<<tc<<": "<<setprecision(10)<<pval<<"\n";
		}

	}
	return 0;
}

