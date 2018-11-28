#include<iostream>
#include<string.h>
using namespace std;


int main(){
	int t, cs=1;
	double c, f, x, s, m, n;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
	cin>>t;
	while(t--) {
		cin>>c>>f>>x;
		s=m=0;
		n=2;
		while(x>m) {
			if( m < c ) {
				if( c < x ) {
					s+=(c-m)/n;
					m=c;
				} else {
					s+=(x-m)/n;
					m=x;
					break;
				}
			}
			if( (x-m)/n <= (x-(m-c))/(n+f) ) {
				s+=(x-m)/n;
				m=x;
				break;
			}
			m-=c;
			n+=f;
		}
		printf("Case #%d: %.7lf\n",cs,s);
		cs++;
	}

	return 0;
}
