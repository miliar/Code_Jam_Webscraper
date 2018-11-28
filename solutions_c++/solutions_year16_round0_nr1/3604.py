#include <bits/stdc++.h>
#define FOR(i,a) for(i = 0; i < a; i++)
#define FR(i,a,b) for(i = a; i < b; i++) 
#define F first
#define S second
typedef long long ll;
using namespace std;
int main(){
	long long i,j,cifra,n,T,test;
	long long k, k1;
	// freopen("a.in","r",stdin);
	// freopen("a.out","w",stdout);
	cin >> T;
	FR(test,1,T+1){
		cin >> n;
		if(n==0){
			cout << "Case #" << test << ": INSOMNIA" << endl;
		}else{
			bool a[10] = {false};
			i = 1;
			bool lol = false;
			while(!lol){
				lol = true;
				k = i * n;
				i++;
				k1 = k;
				while(k1>0){
					cifra = k1%10;
					k1 /= 10;
					a[cifra] = true;
				}
				FOR(j,10){
					if(!a[j]){
						lol = false;
						break;
					}
				}
			}
			cout << "Case #" << test << ": " << k << endl;
		}
	}
	return 0;
}