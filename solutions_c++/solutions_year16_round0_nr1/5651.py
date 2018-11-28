/* My First Template  
   :P
*/
#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define ll long long int
#define pb push_back
#define mk make_pair
ll power(ll a, ll b) {
ll x = 1, y = a;
    while(b > 0) {
        if(b%2 == 1) {
            x=(x*y);
            if(x>mod) x%=mod;
        }
        y = (y*y);
        if(y>mod) y%=mod;
        b /= 2;
    }
    return x;
}
int main() 
{
	freopen("input1.in","r",stdin);
	freopen("output1.txt","w",stdout);
	int t,tc;
	cin>>t;
	tc = 1;
	while(t--) {
		int n,k;
		cin>>n;
		if(n == 0) {
			cout<<"Case #"<<tc<<": "<<"INSOMNIA"<<endl;
			tc++;
			continue;
		}
		int a[10] = {0},i = 1;
		int c = 0;
		while(1) {
			k = n*i;
			while(k) {
				if(!a[k%10]) {
					a[k%10]++;
					c++;
				}
				k /= 10;
			}
			if(c == 10) break;
			i++;
		} 
		k = n*i;
		cout<<"Case #"<<tc<<": "<<k<<endl;
		tc++;
	}
	return 0;
}

