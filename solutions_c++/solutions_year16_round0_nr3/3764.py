#include <limits>
#include <time.h>
#include <iostream>
#include <math.h>
#include <vector>
#include <sstream>

using namespace std;
typedef unsigned long long int ll;

ll maxv[33] = {
		0x00, 0x00, 0x03, 0x07, 0x0f, 0x1f, 0x3f, 0x7f, 0xff,
		0x01ff, 0x03ff, 0x07ff, 0x0fff, 0x1fff, 0x3fff, 0x7fff, 0xffff,
		0x01ffff, 0x03ffff, 0x07ffff, 0x0fffff, 0x1fffff, 0x3fffff, 0x7fffff, 0xffffff,
		0x01ffffff, 0x03ffffff, 0x07ffffff, 0x0fffffff, 0x1fffffff, 0x3fffffff, 0x7fffffff, 0xffffffff
};


pair<ll, ll> minmax[33] = {make_pair(0, 0),
		make_pair(0,0),
		make_pair(3, 3), //2
		make_pair(5, 7), //3
		make_pair(9, 15), //4
		make_pair(17, 31), //5
		make_pair(33, 63), //6
		make_pair(65, 127), //7
		make_pair(129, 255), //8
		make_pair(257, 511), //9
		make_pair(513, 1023), //10

		make_pair(1025, 2047), //11
		make_pair(2049, 4095), //12
		make_pair(4097, 8191), //13
		make_pair(8193, 16383), //14
		make_pair(16385, 32767), //15
		make_pair(32769, 65535), //16
		make_pair(65537, 131071), //17
		make_pair(131073, 262143), //18
		make_pair(262145, 524287), //19
		make_pair(524289, 1048575), //20

		make_pair(1048577, 2097151), //21
		make_pair(2097153, 4194303), //22
		make_pair(4194305, 8388607), //23
		make_pair(8388609, 16777215), //24
		make_pair(16777217, 33554431), //25
		make_pair(33554433, 67108863), //26
		make_pair(67108865, 134217727), //27
		make_pair(134217729, 268435455), //28
		make_pair(268435457, 536870911), //29
		make_pair(536870913, 1073741823), //30

		make_pair(1073741825, 2147483647), //31
		make_pair(2147483649, 4294967295) //32
};

ll mpow(int n, int e) {
	ll ans=1;
	while(e--) {
		ans = ans*n;
	}
	return ans;
}

bool isPrime(ll n){

    if(n < 2) return false;
    if(n == 2) return true;
    if(n % 2 == 0) return false;
    for(ll i=3; (i*i)<=n; i+=2){
        if(n % i == 0 ) return false;
    }
    return true;

}

ll getbaserep( ll n, int base) {
	ll value=0;
	ll i = 0;
	while(n) {
		int d = n & 0x01;
		if(d)
			value += mpow(base, i);
		n=n>>1;
		++i;
	}

	return value;
}

string getbinstr(ll n) {
	stringstream ss, ret;
	while(n) {
		int d = n & 0x01;
		ss<<d;
		n = n>>1;
	}
	string str = ss.str();
	for(int i=str.length()-1;i>=0; --i) {
		ret<<str[i];
	}
	return ret.str();
}

bool checkPrime(ll n, vector<ll>& basec) {
	bool isP = false;
	for(int i=2; i<=10; ++i) {
		ll num = getbaserep(n, i);
		basec[i] = num;
		if(isPrime(num)) {
			isP = true;
			break;
		}
	}

	return isP;
}

bool checkfirstlast(ll n) {
	return n&0x01 == 0x01;
}

ll getdivisor(ll n) {
	ll ans = 1;
	for(ll i=2; i<n; ++i) {
		if(n%i == 0 ) {
			ans = i;
			break;
		}
	}

	return ans;
}
int main() {
	int n;
	int t;
	cin>>t;
	cin>>n;
	int j;
	cin>>j;

	ll start = minmax[n].first;
	ll end = minmax[n].second;

	for(int i=1; i<=t; ++i) {
		cout<<"Case #"<<i<<":\n";

		while(start <= end && j > 0) {
			vector<ll> basec(11, 0);
			if(!checkPrime(start, basec) && checkfirstlast(start)) {
				cout<<getbinstr(start);
				for(int i=2;i<=10; ++i) {
					cout<<" "<<getdivisor(basec[i]);
				}
				cout<<"\n";
				j--;
			}
			start++;
		}
	}



	return 0;
}
