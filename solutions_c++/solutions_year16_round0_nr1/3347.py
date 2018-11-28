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

ll modpow(ll base, ll exponent,ll modulus){
	if(base==0&&exponent==0)return 0;
	ll result = 1;
	while (exponent > 0){
		if (exponent % 2 == 1)
		    result = (result * base) % modulus;
		exponent = exponent >> 1;
		base = (base * base) % modulus;
	}
	return result;
}

ll N; bool visited[11]; void flush(void){ for(int i = 0; i < 10; i++) visited[i] = false;}

void go(ll x){
	while(x){
		visited[x % 10] = true;
		x /= 10;
	}
}

bool check(void){
	for(int i = 0; i < 10; i++) if(!visited[i]) return false;
	return true;
}

inline void ReadInput(void){
	sl(N);
}

inline void solve(int t){
	if(N == 0){
		printf("Case #%d: INSOMNIA\n", t);
		return;
	}
	ll curr = N;
	while(1){
		go(curr);
		if(check()){
			printf("Case #%d: %lld\n", t, curr);
			return;
		}
		curr += N;
	}
}

inline void Refresh(void){
	
}

int main()
{	
	//ios_base::sync_with_stdio(false);
	int t; si(t);
	for(int i = 1; i <= t; i++){
		flush();
		ReadInput();
		solve(i);
	}
    return 0;
}

// U COME AT THE KING, BETTER NOT MISS !!!