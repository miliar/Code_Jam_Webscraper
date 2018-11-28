#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
#include <fstream>

using namespace std;

typedef long long ll;

int main(){ 
	ofstream fout;
	fout.open ("ayylmao.txt");
	ifstream fin;
	fin.open ("A-large.in");

	int t; fin>>t;
	for(int i = 1; i <= t; i++) {
		ll n; fin>>n;
		ll m = n;
		fout<<"Case #"<<i<<": ";
		if(n==0) {
			fout<<"INSOMNIA"<<endl;
			continue;
		}
		int num = 0;
		while(num != 1023) {
			int x = m;
			while(x > 0) {
				num ^= (-1 ^ num) & (1 << x%10);
				x /= 10;
			}
			//bitset<10> y(num);
			//cout<<y<<endl;
			m += n;
		}
		fout<<m-n<<endl;
	}
	return 0;
}