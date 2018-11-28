#include <bits/stdc++.h>
#define FOR(i,a) for(i = 0; i < a; i++)
#define FR(i,a,b) for(i = a; i < b; i++) 
#define F first
#define S second
typedef long long ll;
using namespace std;
int main(){
	long long i,k,c,s,T,test;
	// freopen("a.in","r",stdin);
	// freopen("a.out","w",stdout);
	cin >> T;
	FR(test,1,T+1){
		cin >> k >> c >> s;

		ll cnt=1;

		for (i=0;i<c-1;i++)
			cnt*=k;

		cout << "Case #" << test << ": ";

		for (i=0;i<s;i++)
			cout << i*cnt + 1 << " ";

		cout << endl;
	}
	return 0;
}
