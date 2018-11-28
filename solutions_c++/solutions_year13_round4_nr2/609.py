#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <assert.h>
using namespace std;
typedef long long LL;
LL countA(LL r, LL dt, LL sum){
	if (r != 0){
		return countA((r-1)>>1, dt>>1, sum + (dt>>1));
	}else{
		return sum;
	}
}
LL n;
LL countB(LL r, LL turn){
	//cout<<r<<' '<<turn<<endl;
	//assert(turn >= 0);
	if (r ==((1<<turn)-1)){
		return (1<<turn)-1;
	}else{
		return countB((r+1)>>1, turn-1);
	}
}
int main(){
	freopen("B.in","r", stdin);
	freopen("B.out","w",stdout);
	int T;
	int cas = 0;
	cin>>T;
	while (T--){
		LL p;
		cin>>n>>p;
		p--;
		LL num = (1<<n);
		LL l = 0, r = num;
		while (l+1<r){
			LL m= ((l+r)>>1);
			LL rs = countA(m, num, 0);
			if (rs > p){
				r = m;
			}else{
				l = m;
			}
		}
		LL ans1 = l;
		l = 0, r = num;
		while (l+1<r){
			LL m= ((l+r)>>1);
			LL rs = countB(m, n);
			if (rs <= p){
				l = m;
			}else{
				r = m;
			}
		}
		LL ans2 = l;
		cas++;
		cout<<"Case #"<<cas<<": ";
		cout<<ans1<<' '<<ans2<<endl;
	}
	return 0;
}
