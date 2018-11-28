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

ll K, C, S;


inline void ReadInput(void){
	sl(K); sl(C); sl(S);
}

inline void solve(int t){
	cout << "Case #" << t << ": ";
	ll x = pow(K, C - 1);
	for(int i = 1; i <= K; i++){
		cout << 1 + 0LL + (i - 1) * x << " ";
	}
	cout << endl;
}

inline void Refresh(void){
	
}

int main()
{	
	//ios_base::sync_with_stdio(false);
	int t; si(t);
	for(int i = 1; i <= t; i++){
		ReadInput();
		solve(i);
    }
    return 0;
}

// U COME AT THE KING, BETTER NOT MISS !!!