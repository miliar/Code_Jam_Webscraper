#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
using namespace std;

long long A,B,T;
int p[20],l;

bool check (long long n){
	int l=0;
	while (n!=0){
		p[l++]=n%10;
		n/=10;
	}
	bool c=1;
	for (int i=0;i<l;++i){
		c = c&&(p[i]==p[l-i-1]);
	}
	return c;
}

int main(){
	cin >> T;
	for (int t=1;t<=T;++t){
		cin >> A >> B;
		long long s=1,ta=1000000000,mid=9;
		while (mid != (s+ta)/2){
			mid=(s+ta)/2;
			if (A<=mid*mid)
				ta=mid;
			else if (mid*mid<A)
				s=mid+1;
		}
		mid=s;
		if (mid*mid<A){
			mid+=1;
		}
		long long temp,ans=0;
		for (;mid*mid<=B;++mid){
			if (check(mid)&&check(mid*mid)){
				++ans;
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
}
