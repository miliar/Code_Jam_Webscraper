/*
***************************************************************************************************************

							Author : Yash Sadhwani

**************************************************************************************************************
*/
#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)
#define sd(x) scanf("%lf",&x)
#define sc(x) scanf("%c",&x)
#define ss(x) scanf("%s",x)
#define vl vector<ll>
#define vi vector<int>
#define pb push_back
#define mod 1000000007

	
#define MAXN 200110
#define SQRT 330
#define ls (node<<1)
#define rs ((node<<1)+1)
#define ii pair<int,int>
#define F first
#define S second

/*
long long mul(long long a,long long b,long long c);
long long mod(long long a,long long b,long long c){
    long long x=1,y=a; 
    while(b > 0){
        if(b%2 == 1){
            x=mul(x,y,c);
        }
        y = mul(y,y,c); 
        b /= 2;
    }
    return x%c;
}
 
long long mul(long long a,long long b,long long c){
    long long x = 0,y=a%c;
    while(b > 0){
        if(b%2 == 1){
            x = (x+y)%c;
        }
        y = (y*2)%c;
        b /= 2;
    }
    return x%c;
}
int isprime(ll n,ll acc){
	if(n==2||n==3){
		return 1;
	}
	srand(time(NULL));
	ll s=0,t=n-1;
	while(1){
		if(t%2==1||(t=t/2)==0){
			break;
		}
		s++;
	}
	ll d=((n-1)/(ll)pow(2,s));
	for(ll i=0;i<acc;i++){
		ll flag=0;
		ll a=(rand()%(n-3))+2;
		ll t=mod(a,d,n);
		if(t==1||t==n-1||t==-1){
			continue;
		}
		for(ll j=0;j<s-1;j++){
			t=mul(t,t,n);
			if(t==1){
				return 0;
			}
			if(t==n-1||t==-1){
				flag=1;
				break;
			}
		}
		if(flag==1){
			continue;
		}
		return 0;
	}
	return 1;
}*/

ll give(ll mask, int n, int b){
	ll ret = 0, curr = 1;
	for(int i = 0; i < n; i++){
		if(mask & (1LL << i)) ret += curr;
		curr *= b;
	}
	return ret;
}

inline void ReadInput(void){
	int n, b; si(n); si(b);
}

inline void solve(void){
	ll max_mask = (1LL << 14);
	int cnt = 0;
	for(ll mask = 0; mask < max_mask; mask++){
		ll nmask = (mask * 2) + 1 + (1LL << 15);
		bool flag = false;
		vl u; u.clear(); u.pb(give(nmask, 16, 10));
		for(int b = 2; b <= 10; b++){
			ll k = give(nmask, 16, b);
			for(int t = 2; t < min(100LL, k); t++){
				if(k % t == 0){
					u.pb(t);
					break;
				}
			}
		}
		if(u.size() == 10){
			cnt++;
			for(int i = 0; i < 10; i++) cout << u[i] << " "; cout << endl;
			if(cnt == 50) return;
		}
	}
}

inline void Refresh(void){
	
}

int main()
{	
	//ios_base::sync_with_stdio(false);
	int t; si(t);
	cout << "Case #1:\n";
	ReadInput();
	solve();
    return 0;
}

// U COME AT THE KING, BETTER NOT MISS !!!