#include <iostream>
#include <fstream>
#include <bitset>
using namespace std;

int main()
{
	ifstream fin("lottery.in");
	ofstream fout("lottery.out");
	int t; fin >> t;
	for(int i=0; i<t; ++i) {
		unsigned a,b,c; fin >> a >> b >> c;
		long long ans=0;
		for(unsigned x=0; x<a; ++x) {
			for(unsigned y=0; y<b; ++y) {
				if((x & y) < c) {
					++ans;
				}
			}
		}
		fout << "Case #" << i+1 << ": " << ans << endl;
	}
}
