// __________ AUTHOR INFO __________
// Name/    Khaled Alam
// Email/   khaledalam.net@gmail.com
// Insta/   @MrKhaledAlam
// Twitter/ @Mr_KhaledAlam
// Website/ KhaledAlam.net
//__________________________________

//#include <bits/stdc++.h>
//#include <conio.h>
//#include <windows.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <algorithm>
#include <limits>
#include <vector>
#include <set>
#include <cmath>
#include <math.h>
#include <string>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <utility>
#include <map>
#include <ctime>
#include <time.h>
#include <bitset>
#include <iomanip>
#include <cstring>
#include <climits>
#include <complex>
#include <typeinfo>
#include <numeric>
#include <functional>
//=====================
using namespace std;

#define I int
#define UI unsigned int
#define LL long long
#define ULL unsigned long long
#define STG string
#define CHR char
#define V vector
#define oo ((const int)1e9)
#define MOD ((const int)1e9+7)
#define PI 3.1415926536
#define SZ(X) (int)X.size()
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
#define ODD(n) (n&1)
#define ALL(C) C.begin(), C.end()
#define rALL(C) C.rbegin(), C.rend()
#define rSORT(C) sort(ALL(C), std::greater<LL>())
#define FOR(V,A,Z,P)  for(I V=A;V<Z;V+=P)
#define FORb(V,A,Z,P) for(I V=A;V>=Z;V-=P)
#define IOS ios_base::sync_with_stdio(0);
#define SET(A,V) memset(A,V,sizeof A)
#define iFILE(N) freopen(#N, "r", stdin)
#define oFILE(N) freopen(#N, "w", stdout)
#define TM cerr<<"Time elapsed: "<<clock()/1000<<" ms\n";
//#define MX
//I vis[100];

//---------START--------//

I p=1,c,temp;
I digs[10];
I org;

I digCount(I y ){
	I cnt=0;
	while(y>0){
	c = y%10;
	y/=10;
	cnt++;
	}
	return cnt;
}


LL dig(I n){
	p++;
	temp = n;
	I h = digCount(temp);

	FOR(u,0,h,1){

			c = temp%10;
			temp/=10;

			if(digs[c] == 0)digs[c]=1;

			}

	if(count(digs,digs+10 , 1) < 10){

			return (dig(p*org));

	}else{
		return n;
	}

return n;
}




I main(){

iFILE(input.txt);
oFILE(output.txt);

	I t,n;

	scanf("%d",&t);

	FOR(i,0,t,1){

		scanf("%d",&n);
		org = n;
		if(n == 0){
			cout<<"Case #"<<i+1<<": INSOMNIA\n";
			continue;
		}
		else{
			FOR(j,0,10,1)digs[j]=0;
		cout<<"Case #"<<i+1<<": "<<dig(n)<<"\n";
		}
		p = 1;
	}

return 0;
}
