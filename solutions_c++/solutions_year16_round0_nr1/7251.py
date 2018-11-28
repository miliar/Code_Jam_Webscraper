#include <iostream>
#include <cstring>
using namespace std;

#define MAX_MUL 1000
#define ULL unsigned long long

int main() {
	ULL kases, N;
	cin >> kases;
	for(int T=1; T<=kases; T++) {
		ULL found[10], count=0;
		memset(found, 0, sizeof(found));
	
		cin >> N;
		cout << "Case #" << T << ": ";
		for(int i=1; i<MAX_MUL; i++) {
			ULL K = N*i;
			while(K) {
				found[K%10] = 1;
				K /= 10;
			}
			
			count = 0;
			for(int i=0; i<10; i++) {
				if ( found[i] )
					count++;
			}
			
			if ( count == 10 ) {
				cout << N*i << endl;
				break;
			}
		}
		
		if ( count < 10 ) {
			cout << "INSOMNIA" << endl;
		}
	}
	return 0;
}