#include <iostream>
#include <cmath>

using namespace std;

int main(){
	long K;
	cin >> K;
	for(int k = 0; k< K; ++k){
		cout << "Case #" << k+1 << ": ";
		unsigned long long t,r;
		long long count = 0;
		cin >> r >> t;
		
		do{ 
			unsigned long long amount = (r+1)*(r+1) - (r*r);
			if(amount > t) break;
			t -= amount;//take first ring
			count++;
			r+=2;
		}
		while(t > 0);
		cout << count << endl;
	}
}