#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>

#include <math.h>
#include <vector>
#include <deque>
#include <set>
#include <algorithm>

using namespace std;

typedef __int128_t L128;
typedef __uint128_t UL128;

typedef long long LL;
typedef unsigned long long ULL;

LL baseN(LL a, LL n) {
    LL ret=0;
    LL place=1;
    while(a!=0) {
        if(a%2)
            ret += place;
        a/=2;
        place *= n;
    }
    
    return ret;
}

void printBin(LL n) {
    
    deque<int> v;
    while(n!=0) {
        if(n%2) {
            v.push_front(1);
        }
        else {
            v.push_front(0);
        }
        n/=2;
    }
    
    for(int i=0; i<v.size(); i++) {
        cout << v[i];
    }
}

LL isPrime(LL n) {
    
    for(LL i=2; i*i<=n; i++) {
        if(n%i==0)
            return i;
    }
    
    return 1;
}

bool isCoin(LL n) {
    
    //cout << n << " ";
    bool bCoin = true;
    stringstream str;
    
    //str << n << " ";
    for(LL i=2; i<=10; i++) {
        LL val = baseN(n, i);
        LL pp = isPrime(val);
        str << pp << " ";
        if(pp == 1) {
            bCoin = false;
        }
        //cout << val << ":" << isPrime(val) << " ";
    }
    
    if(bCoin) {
        printBin(n);
        cout << " " << str.str() << endl;
        return true;
    }
    
    return false;
}

LL findCoin(LL i, LL bits) {
    LL ff = 1;
    ff = ff<<(bits-1);
    ff += 1;
        
    LL coin = ((i<<1)|ff);
    if(isCoin(coin)) {
        return 1;
    }
    
    return 0;
}

int main(int argc, char** argv) {

	LL N,T;cin>>T;

	for(LL t=1; t<=T; t++)
	{
        LL bits;cin>>bits;
		cin>>N;
        
        cout << "Case #" << t << ": " << endl;
        
        // Find the coins!
        LL coin=0;
        for(LL i=0; i<0xffffffff; i++) {
            coin += findCoin(i, bits);
            if(coin>=N)
                break;
        }
        
        //for(LL i=2; i<=10; i++)
        //    cout << baseN(N, i) << endl;
	}

	return 0;
}
