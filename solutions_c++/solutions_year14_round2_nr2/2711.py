#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main () {
	int T;
	cin>>T;
	int cases = 1;
	while (cases <= T) {
		int A, B, K;
		cin>>A>>B>>K;
		int count = 0;
		for (int i=0; i<A; i++) {
			for (int j=0; j<B; j++) {
				int temp = j&i;
				if (temp < K) {
					count++;
				}
			}
		}
		cout<<"Case #"<<cases<<": "<<count<<"\n";
		cases++;
	}
	return 0;
}