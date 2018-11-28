#include <bits/stdc++.h>

using namespace std;

#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
#define forn(i, n) for (int i = 0; i < (n); i++)
typedef long long ll;

int main(){
	int X, R, C, T;
	scanf("%d", &T);
	for(int i=1; i<=T; ++i){
		scanf("%d %d %d", &X, &R, &C);
		printf("Case #%d: ", i);
		if(R>C) swap(R, C);
		if(X==1){
			printf("GABRIEL\n");
		}else{
			if(X==4){
				if((R==3 and C==4) or (R==4 and C==4)) printf("GABRIEL\n");
				else printf("RICHARD\n");
		  	}else{
			    if(X==2){
					if((R==1 and (C==1 or C==3)) or (R==3 and C==3)) printf("RICHARD\n");
					else printf("GABRIEL\n");
				}else{
					if((R==3 and (C==3 or C==4)) or (R==2 and C==3)) printf("GABRIEL\n");
					else printf("RICHARD\n");
				}
			}
		}
	}
    return 0;
}
