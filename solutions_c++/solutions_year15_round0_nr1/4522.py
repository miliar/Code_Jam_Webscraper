//In the name of God
#include <bits/stdc++.h>
using namespace std;
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
#define Rof(i,a,b) for(int (i)=(a);(i) >= (b); --(i))
#define mkp make_pair
#define XX first
#define YY second
#define pb push_back
const int Maxn = 2e5 + 9;
char S[Maxn];
int arr[Maxn];
int main(){
	freopen("file.out","w",stdout);
	int t;
	cin >> t;
	int tc = 0;
	while(t--){
		int n;
		scanf("%d",&n);
		scanf("%s",S);
		For(i,0,1001){
			int cnt = i;
			bool flag = 0;
			For(j,0,n+1){
				if(cnt >= j)
					cnt+= S[j] - '0';
				else
					flag = 1;
			}
			if(flag)
				continue;
			printf("Case #%d: %d\n",++tc,i);
			break;
		}
	}
}
