# include <bits/stdc++.h>

# define ff first
# define ss second
# define mp(x,y) make_pair(x,y)
# define tr(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
# define MAXN 1009

template<typename A, typename B> inline void amax(A &x, B y) {if(x < y) x = y;}
template<typename A, typename B> inline void amin(A &x, B y) {if(!(x < y)) x = y;}

typedef long long lld;

using namespace std;

int n, t;
char s[MAXN];
int sz;

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	scanf("%d",&t);
	
	int ans;
	int aud;
	
	for(int u=0; u<t; u++){
		scanf("%d %s",&n,s);
		
		sz = strlen(s);
		
		ans = 0;
		aud = s[0] - '0';
		
		for(int i=1; i<sz; i++){
			if(aud < i){
				ans++;
				aud++;
			}
			
			aud += s[i] - '0';
		}
		
		printf("Case #%d: %d\n",u+1,ans);
	}
}
