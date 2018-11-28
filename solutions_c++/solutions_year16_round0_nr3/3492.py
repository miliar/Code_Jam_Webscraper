#include <bits/stdc++.h>
#define ll unsigned long long
using namespace std;
ll po(int a, int b){
	ll r = 1;
	while(b>0){
		if(b&1)
			r = r*a;
		a = a*a;
		b/=2;
	}
	return r;
}
ll bin(ll num){
    ll res = 0;
    while(num>0){
    	if(num%2==1){
    		res += 1;
    	}
    	res *= 10;
    	num /= 2;
    }
    res /= 10;
    ll rev= 0;
    while(res != 0) {
            ll remainder = res%10;
            rev = rev*10 + remainder;
            res/=10;
        }
    return rev;
}
ll b2(ll n){
    ll decimal=0, i=0, rem;
    while (n!=0){
        rem = n%10;
        n/=10;
        decimal += rem*po(2,i);
        ++i;
    }
    return decimal;
}
ll b3(ll n){
    ll decimal=0, i=0, rem;
    while (n!=0){
        rem = n%10;
        n/=10;
        decimal += rem*po(3,i);
        ++i;
    }
    return decimal;
}
ll b4(ll n){
    ll decimal=0, i=0, rem;
    while (n!=0){
        rem = n%10;
        n/=10;
        decimal += rem*po(4,i);
        ++i;
    }
    return decimal;
}
ll b5(ll n){
    ll decimal=0, i=0, rem;
    while (n!=0){
        rem = n%10;
        n/=10;
        decimal += rem*po(5,i);
        ++i;
    }
    return decimal;
}
ll b6(ll n){
    ll decimal=0, i=0, rem;
    while (n!=0){
        rem = n%10;
        n/=10;
        decimal += rem*po(6,i);
        ++i;
    }
    return decimal;
}
ll b7(ll n){
    ll decimal=0, i=0, rem;
    while (n!=0){
        rem = n%10;
        n/=10;
        decimal += rem*po(7,i);
        ++i;
    }
    return decimal;
}
ll b8(ll n){
    ll decimal=0, i=0, rem;
    while (n!=0){
        rem = n%10;
        n/=10;
        decimal += rem*po(8,i);
        ++i;
    }
    return decimal;
}
ll b9(ll n){
    ll decimal=0, i=0, rem;
    while (n!=0){
        rem = n%10;
        n/=10;
        decimal += rem*po(9,i);
        ++i;
    }
    return decimal;
}
bool cc(ll a){
	if(a%2==0)
		return true;
	for(int i = 3; i<=sqrt(a); i+=2){
		if(a%i==0)
			return true;
	}
	return false;
}
ll div(ll a){
	for(int i = 2; i<=sqrt(a); i++){
		if(a%i==0)
			return i;
	}
	return -1;
}
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin>>t;
	for(int uv = 1; uv<=t; uv++){
		int n, k, co = 0;
		cin>>n>>k;
		cout<<"Case #1:"<<endl;
		for(ll z = pow(2, n-1)+1; z<pow(2, n) && co<k; z+=2){
			ll b, c, d, e, f, g, h, i, j;
			ll y = bin(z);
			b = b2(y), c = b3(y), d = b4(y), e = b5(y);
			f = b6(y), g = b7(y), h = b8(y), i = b9(y), j = y;
//			cout<<b<<" "<<c<<" "<<d<<" "<<e<<" "<<f<<" "<<g<<" "<<h<<" "<<i<<" "<<j<<endl;
			if(cc(b) && cc(c) && cc(d) && cc(e) && cc(f) && cc(g) && cc(h) && cc(i) && cc(j)){
	//			cout<<b<<" "<<c<<" "<<d<<" "<<e<<" "<<f<<" "<<g<<" "<<h<<" "<<i<<" "<<j<<endl;

				cout<<y<<" "<<div(b)<<" "<<div(c)<<" "<<div(d)<<" "<<div(e)<<" "<<div(f)<<" "<<div(g)<<" "<<div(h)<<" "<<div(i)<<" "<<div(j)<<endl;
				co++;
			}
		}
	}
	return 0;
}
