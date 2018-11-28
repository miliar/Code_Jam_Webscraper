#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <cstdio>

using namespace std;

#define BYTETOBINARYPATTERN "%d%d%d%d%d%d%d%d"
#define BYTETOBINARY(byte)  \
  (byte & 0x80 ? 1 : 0), \
  (byte & 0x40 ? 1 : 0), \
  (byte & 0x20 ? 1 : 0), \
  (byte & 0x10 ? 1 : 0), \
  (byte & 0x08 ? 1 : 0), \
  (byte & 0x04 ? 1 : 0), \
  (byte & 0x02 ? 1 : 0), \
  (byte & 0x01 ? 1 : 0) 

int modulo(int a,int b,int c){
    long long x=1,y=a; // long long is taken to avoid overflow of intermediate results
    while(b > 0){
        if(b%2 == 1){
            x=(x*y)%c;
        }
        y = (y*y)%c; // squaring the base
        b /= 2;
    }
    return x%c;
}

long long mulmod(long long a,long long b,long long c){
    long long x = 0,y=a%c;
    while(b > 0){
        if(b%2 == 1){
            x = (x+y)%c;
        }
        y = (y*2)%c;
        b /= 2;
    }
    return x%c;
}

bool Miller(long long p,int iteration){
    if(p<2){
        return false;
    }
    if(p!=2 && p%2==0){
        return false;
    }
    long long s=p-1;
    while(s%2==0){
        s/=2;
    }
    for(int i=0;i<iteration;i++){
        long long a=rand()%(p-1)+1,temp=s;
        long long mod=modulo(a,temp,p);
        while(temp!=p-1 && mod!=1 && mod!=p-1){
            mod=mulmod(mod,mod,p);
            temp *= 2;
        }
        if(mod!=p-1 && temp%2==0){
            return false;
        }
    }
    return true;
}

long long first_divisor(long long p) {
	// returns 0 if no divisor found!
	for (int i = 2; i < sqrt(p) + 1; ++i) {
		if (p % i == 0) {
			return i;
		}
	}
	return 0;
}


int main() {
	int count = 0;
	char buf[20];

	for (int i = 32768; i < 65536; ++i) {		
		sprintf(buf, BYTETOBINARYPATTERN""BYTETOBINARYPATTERN,
  BYTETOBINARY(i>>8), BYTETOBINARY(i));
//		cout << buf << endl;
//		cout << stoull(buf, 0, 2) << endl;
		
		int result = 1;

		for (int i = 2; i <= 10; ++i) {
			long long n = stoll(buf, 0, i);
			if (Miller(n, 20)) {
				result *= 0;
			}
		}

		if (result == 1 && buf[15] == '1') {
			vector<int> divs;
			bool good = true;
			for (int i = 2; i <= 10; ++i) {
				long long n = stoll(buf, 0, i);
				int di = first_divisor(n);
				if (di == 0)
					good = false;
				divs.push_back(di);
			}
			if (good) {
				cout << stoll(buf, 0, 10);
				for (int i = 0; i < divs.size(); ++i) {
					cout << " " << divs[i];
				}
				cout << endl;
				++count;
			}
		if (count == 50)
			return 0;
		}
	}

	return 0;
}
