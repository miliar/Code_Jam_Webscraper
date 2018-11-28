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


char str[MAXN]; int N, p;

inline void ReadInput(void){
	ss(str);
}

inline void solve(int t){
	N = strlen(str);
	char c = str[0]; p = 1;
	for(int i = 1; i < N; i++){
		if(str[i] != c){
			c = str[i]; p++;
		}
	}
	if(str[N - 1] == '+') printf("Case #%d: %d\n", t, p - 1);
	else printf("Case #%d: %d\n", t, p);
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