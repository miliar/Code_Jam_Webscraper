#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

const int N = 1005;

#define fo(i , st , en) for (int i = st; i <= en; i++)
#define Me(x , y) memset(x , y , sizeof(x))

int t , maxs;
char s[N];

int main(){
	freopen("1.in" , "r" , stdin);
	freopen("1.out" , "w" , stdout);
	scanf("%d" , &t);
	fo (i , 1 , t){
		scanf("%d%s" , &maxs , s); int cur = 0 , ans = 0;
		fo (j , 0 , maxs){
			ans = max(j - cur , ans);
			cur += s[j] - '0';
		}
		printf("Case #%d: %d\n" , i , ans);
	}
	return 0;
}
