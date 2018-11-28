#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

const int N = 2005;

#define fo(i , st , en) for (int i = st; i <= en; i++)
#define fd(i , st , en) for (int i = st; i >= en; i--)
#define Me(x , y) memset(x , y , sizeof(x))
#define Mc(x , y) memcpy(x , y , sizeof(x))

int a[N];
int t , n;

int main(){
	freopen("2.in" , "r" , stdin);
	freopen("2.out" , "w" , stdout);
	scanf("%d" , &t);
	fo (i , 1 , t){
		scanf("%d" , &n); int x; Me(a , 0);
		fo (j , 1 , n) scanf("%d" , a + j);
		int temp = 0 , ans = 1000;
		fo (j , 1 , 1000){
			temp = 0;
			fo (k , 1 , n) temp += (a[k] + j - 1) / j - 1;
			ans = min(ans , temp + j);
		}
		printf("Case #%d: %d\n" , i , ans);
	}
	return 0;
}
