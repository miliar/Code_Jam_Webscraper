#include <iostream>
#include <fstream>
using namespace std;
long long gcd(long long p, long long q){
	if (p == q) return p;
	if (p-q > q) return gcd(p-q, q);
	else return gcd(q, p-q);
}
int main(){
	long long T, p, q;
	char c;
	ofstream SaveFile("a.txt");
	cin>>T;
	for (int n = 0; n < T; ++n){
		SaveFile<<"Case #"<<n+1<<": ";
		cin>>p>>c>>q;
		if (p > q) SaveFile<<"impossible"<<endl;
		else{
			long long m = gcd(q, p);
			p /= m;
			q /= m;
			long long qq = q;
			int k = 0;
			while (q % 2 == 0){
				if (q > p) ++k;
				q/=2;
			} 
			if (q == 1){
				SaveFile<<k<<endl;
			}
			else{
				SaveFile<<"impossible"<<endl;
			}
		}
	}
	return 0;
}