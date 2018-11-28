#include <iostream>
using namespace std;

int main()
{
	int T;
	long N;
	cin >> T;
	for(int i=1; i<=T;i++) {
		cin >> N;
		cout << "Case #" << i << ": ";
		if(N==0) {
			cout << "INSOMNIA\n";
			continue;
		}
		bool found[10] = {false};
		int x=-1;
		while(++x < 10) found[x]=false;
		int count=0;
		for(int k=1; k<100;k++) {
			long n = k*N;
			while(n) {
				if (!found[n%10]) {
					found[n%10] = true;
					count++;
					if(count == 10) {
						cout << k*N << endl;
						break;
					}
				}
				n/=10;
			}
		}
		if (count != 10) cout <<"INSOMNIA\n"; 
	}
	return 0;
}