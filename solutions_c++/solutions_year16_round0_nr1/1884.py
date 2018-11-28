#include <bits/stdc++.h>
using namespace std;

#define MAX 1000000000

int main(){	
	int t; cin >> t;
	for(int i=0; i<t; i++){
		long long n, a; cin >> n;
		int mask = 0;
		for(int r = 0; r<MAX && (mask != (1<<10)-1); r++){			
			a = n*(r+1);
			long long b = a;
			while(b){
				mask |= 1<<(b%10);
				b /= 10;
			}
		}	
		if(mask == (1<<10)-1)
			cout << "Case #" << (i+1) << ": " << a << "\n";
		else
			cout << "Case #" << (i+1) << ": INSOMNIA\n";
	}
	return 0;
}
