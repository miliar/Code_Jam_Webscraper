#include <iostream>
#include <cstdint>
#include <cstdio>
using namespace std;

int main() {
	int t = 0, N = 0;
	uint32_t h = 0;
	cin >> t; //read t
	if(t < 1) return 0;
	for(int i = 1; i<=t;i++) {
		cin >> N;
		h = 0;
		if(N == 0) {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
		int j = 1;
		for(; h!=0x3ff; j++) {
			int tmpN = N *j;
			while(tmpN>0) {
				int digit = tmpN%10;
				h |= (0x1<<digit);
				tmpN = tmpN /10;
			}
		}// h == 0x3ff
        cout<<"Case #"<<i<<": "<<N*(j-1)<<endl;
	}
}
