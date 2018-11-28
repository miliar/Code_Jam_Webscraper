#include <iostream>
using namespace std;

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	int A,B,K;
	cin>> T;
	for (int t=0; t<T; t++) {
		cin >> A >> B>> K;
		int count=0;
		for (int i=0; i<A; i++){ 
			for (int j=0; j<B; j++) {
				if ((i&j) < K)
					count++;
			}
		}
		cout << "Case #" << t+1 << ": " << count << endl;
	}
}