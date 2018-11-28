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
int arr[Maxn];
int tc = 0;
void richard(){
	printf("Case #%d: RICHARD\n",++tc);
}
void gabriel(){
	printf("Case #%d: GABRIEL\n",++tc);
}
int main(){
	freopen("file.out","w",stdout);
	int t;
	cin >> t;
	while(t--){
		int n,m,x;
		scanf("%d%d%d",&x,&n,&m);
		if(x == 1){
			gabriel();
			continue;
		}
		if(x ==2 && (n * m) % 2 == 0){
			gabriel();
			continue;
		}
		if(x == 2){
			richard();
			continue;
		}
		else if((n * m) % x || x > max(n,m) || x > min(n,m) * 2){
			richard();
			continue;
		}
		if(x == 3 && (n * m) != 3 && (n * m) % 3 == 0){
			gabriel();
			continue;
		}
		if(x == 3){
			richard();
			continue;
		}
		if(x == 4 && n * m == 8){
			richard();
			continue;
		}
		if(x == 4 && (n * m) % 4 == 0){
			gabriel();
			continue;
		}
	}
	return 0;
}
