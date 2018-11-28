#include<cstdio>
#include<iostream>
#include<cmath>
using namespace std;
long long gcd(long long a, long long b){
	if(b == 0 || a == 0)
		return a+b;
	return gcd(b, a%b);
}
int main(){
	int t;
	cin >> t;
	for(int xx = 1; xx <= t; xx++){
		long long p, q;
		scanf("%lld/%lld", &p, &q);
		long long g = gcd(p, q);
		p /= g;
		q /= g;
		long long ans = 0;
		int l = log2(q);
		if((1 << l) != q)
			ans = -1;
		else {
			while(p < q){
				p *= 2;
				ans++;
			}
		}
		if(ans == -1)
			cout << "Case #" << xx << ": impossible" << endl;
		else cout << "Case #" << xx << ": " << ans << endl;
			
	}
	return 0;
}

