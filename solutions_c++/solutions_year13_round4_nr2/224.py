#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

int main() {
	int kasus;
	scanf("%d",&kasus);
	for (int l=1;l<=kasus;++l) {
		long long round,P;
		cin>>round>>P;
		long long kiri = 0;
		long long kanan = (1LL<<round);
		
		while (kanan-kiri > 1) {
			long long tengah = (kiri+kanan) / 2LL;
			long long p1 = tengah;
			long long p2 = round;
			while (p1 > 0) {
				--p2;
				p1 = (p1-1LL) / 2LL;
			}
			
			if (P > (1LL<<round)-(1LL<<p2)) kiri = tengah;
			else kanan = tengah;
		}
		cout<<"Case #"<<l<<": "<<kiri;
		
		kiri = 0;
		kanan = (1LL<<round);
		while (kanan-kiri > 1) {
			long long tengah = (kiri + kanan) / 2LL;
			long long p1 = (1LL<<round)-1-tengah;
			long long p2 = round;
			while (p1 > 0) {
				--p2;
				p1 = (p1-1LL) / 2LL;
			}
			
			if ((1LL<<p2)-1 < P) kiri = tengah;
			else kanan = tengah;
		}
		cout<<" "<<kiri<<endl;
	}
	//cout<<(1LL<<50LL)<<endl;
	return 0;
}
