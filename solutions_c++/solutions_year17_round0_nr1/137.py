#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
#define ii pair<int,int>
#define vii vector<pair<int,int> >
#define vi vector<int>

int n , k ;
char s[1010] ;

int main(){
    freopen("A_large.in","r",stdin);
    freopen("A_large.out","w",stdout);
	int t ;
	scanf("%d",&t);
	for(int T=1;T<=t;T++){
		scanf("%s %d",s,&k) ;
		n = strlen(s) ;
		int ans = 0 ;
		for(int i=0 ; i+k <= n ; i++){
			if(s[i] == '+') continue ;
			ans++ ;
			for(int j=0;j<k;j++) s[i+j] = ( (s[i+j] == '+') ? '-' : '+' ) ;
		}
		for(int i=0;i<n;i++) if( s[i] == '-' ) ans = -1 ;
		if(ans == -1) printf("Case #%d: IMPOSSIBLE\n", T) ;
		else printf("Case #%d: %d\n",T,ans) ;
	}
	return 0;
}
