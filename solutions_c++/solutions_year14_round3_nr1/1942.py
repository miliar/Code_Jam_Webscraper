#include<iostream>

using namespace std;

typedef unsigned long long ull;

int gcd(ull a, ull b) { if (b == 0) { return a; } else { return gcd(b, a % b); } }
int main() {

	int nCases;
	cin>>nCases;
	
	for(int n=0; n<nCases; n++) {
		cout<<"Case #"<<n+1<<": ";
		ull P,Q;
		char temp;
		cin>>P>>temp>>Q;
		ull G=gcd(P,Q);
		Q/=G;P/=G;
		ull QQ=Q;
		int m=0;
		while(QQ!=1) {
			if(QQ&1) {
				m=-1;
				break;
			}
			QQ=QQ>>1;
			m++;			
		} 
		if(m==-1 || m>40) {
			cout<<"impossible"<<endl;
			continue;
		}
		m=1;
		Q/=2;
		while(P<Q) {
			Q/=2;
			m++;
		}
		
		
		cout<<m<<endl;
		
	}
	
	return 0;
}
