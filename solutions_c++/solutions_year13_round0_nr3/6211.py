#include <cstdio>
#include <iostream>
#include <vector>


#include <cmath>
using namespace std;
#define ll long long

int ii=1;

bool is_pal(ll nn) {
	string num = "";
	// cout << nn << endl;
	while(nn > 0) {
		num = num + (char)('0' + (nn%10));
		nn =  nn / 10;
	}
	int ss = num.size()-1;
	for(int i=0;i<num.size()/2;i++) {
		if(num[i] != num[ss])	
			return false;
			ss--;
	}

	return true;
}

bool pal(ll i) {
	double ss = sqrt(i);
	int aa = sqrt(i);
	if(ss != aa) return false;
	return is_pal(i) and is_pal(sqrt(i));
}

void resolve() {
	ll a, b;
	cin >> a >> b;
	int cont =0;
	for(ll i=a; i<=b;i++)
		if(pal(i)) cont ++;

	printf("Case #%d: %d\n", ii++, cont);
}	

int main () {
	int t;
	cin >> t;
	for(int i=0;i<t;i++) resolve();
}