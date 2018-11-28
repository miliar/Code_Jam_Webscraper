#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define D(x) cout << #x << " = " << (x) << endl;
#define all(x) (x).begin(),(x).end()
long long k,c,s;
long long Pow(long long a,long long b){
	if(!b)
		return 1LL;
	long long r = Pow(a,b/2);
	r *= r;
	if(b&1)
		r *= a;
	return r;
}

int main()
{
    freopen("/home/khaled/file.in","r",stdin);
    freopen("/home/khaled/file.out","w",stdout);
    int T,tc(1);
    cin >> T;
    while(T--){
		cin >> k >> c >> s;
		cout << "Case #" << tc++ << ":";
		for(long long i=1;i<=Pow(k,c);i+=Pow(k,c-1))
			cout << " " << i;
		cout << endl;
    }
    return 0;
}



