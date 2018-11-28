#include <bits/stdc++.h>

long long inv = 301388891;
long long mod = 1000000007;
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
const int INF = (1 << 30);

long long modpow(int a, long long b, long long m) {
    a %= m;
    long long r = 1;
    while (b > 0) {
        if (b & 1) r = (r * 1LL * a) % m;
        a = (a * 1LL * a) % m;
        b >>= 1;
    }
    return r;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int t, x, r, c;
	cin>>t;
	for(int k = 1; k <= t; ++k){
		cin>>x>>r>>c;
		if(x == 1)
			cout<<"Case #"<<k<<": GABRIEL"<<endl;
		else if(x == 2){
			if(r >= x){
				if(c >= x - 1){
					if((r * c) % 2 == 0)
						cout<<"Case #"<<k<<": GABRIEL"<<endl;
					else
					cout<<"Case #"<<k<<": RICHARD"<<endl;
				}
				else
					cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
			else if(c >= x){
				if(r >= x - 1){
					if((r * c) % 2 == 0)
						cout<<"Case #"<<k<<": GABRIEL"<<endl;
					else
						cout<<"Case #"<<k<<": RICHARD"<<endl;
				}
				else
					cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
			else{
				cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
		}
		else if(x == 3){
			if(r >= x){
				if(c >= x - 1){
					if((r * c) % 3 == 0)
						cout<<"Case #"<<k<<": GABRIEL"<<endl;
					else
						cout<<"Case #"<<k<<": RICHARD"<<endl;
				}
				else
					cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
			else if(c >= x){
				if(r >= x - 1){
					if((r * c) % 3 == 0)
						cout<<"Case #"<<k<<": GABRIEL"<<endl;
					else
						cout<<"Case #"<<k<<": RICHARD"<<endl;
				}
				else
					cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
			else{
				cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
		}
		else if(x == 4){
			if(r >= x){
				if(c >= x - 1){
					if((r * c) % 4 == 0)
						cout<<"Case #"<<k<<": GABRIEL"<<endl;
					else
						cout<<"Case #"<<k<<": RICHARD"<<endl;
				}
				else
					cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
			else if(c >= x){
				if(r >= x - 1){
					if((r * c) % 4 == 0)
						cout<<"Case #"<<k<<": GABRIEL"<<endl;
					else
						cout<<"Case #"<<k<<": RICHARD"<<endl;
				}
				else
					cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
			else{
				cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
		}
		else if(x == 5){
			if(r >= x){
				if(c >= x - 1){
					if((r * c) % 5 == 0)
						cout<<"Case #"<<k<<": GABRIEL"<<endl;
					else
						cout<<"Case #"<<k<<": RICHARD"<<endl;
				}
				else
					cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
			else if(c >= x){
				if(r >= x - 1){
					if((r * c) % 5 == 0)
						cout<<"Case #"<<k<<": GABRIEL"<<endl;
					else
						cout<<"Case #"<<k<<": RICHARD"<<endl;
				}
				else
					cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
			else{
				cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
		}
		else if(x == 6){
			if(r >= x){
				if(c >= x - 1){
					if((r * c) % 6 == 0)
						cout<<"Case #"<<k<<": GABRIEL"<<endl;
					else
						cout<<"Case #"<<k<<": RICHARD"<<endl;
				}
				else
					cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
			else if(c >= x){
				if(r >= x - 1){
					if((r * c) % 6 == 0)
						cout<<"Case #"<<k<<": GABRIEL"<<endl;
					else
						cout<<"Case #"<<k<<": RICHARD"<<endl;
				}
				else
					cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
			else{
				cout<<"Case #"<<k<<": RICHARD"<<endl;
			}
		}
		else
			cout<<"Case #"<<k<<": RICHARD"<<endl;

	}
	return 0;
}
