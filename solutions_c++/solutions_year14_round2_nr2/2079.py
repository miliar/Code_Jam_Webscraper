#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  ifstream fin("B.in");
	ofstream fout("B.out");
	int t;
	fin>>t;
	for( int tt=0; tt<t; tt++) {
		int count = 0;
		long long int A,B,K,ans;
		fin>>A>>B>>K;
		for( int i=0; i<A; i++) {
		  for( int j=0; j<B; j++) {
			  ans = i&j;
				if(ans<K) {
				  count++;
				}
			}
		}
			fout<<"Case #"<<tt+1<<": "<<count<<endl;
	}
}