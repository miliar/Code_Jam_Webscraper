#include <stdio.h>
#include <iostream>
#include <vector>
#include <string.h>
#include <map>
#include <queue>
#include <algorithm>
#include <math.h>
#include <set>
#include <stack>
#include <sstream>
//#include <strstream>

using namespace std;

#define N 1005
#define M 1000005
#define P 1005
#define INF  0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
#define LL  long long
#define ULL unsigned long long
#define MOD 1000000007

#define eps 1e-9
#define PI acos(-1.0)
#define MID ((l + r)/2)
#define lx (x<<1)
#define rx ((x<<1)|1)

#define ppi pair<int,int>
#define lowbit(x) (x&(-x))
#define REP(i,n) for(int i=0;i<n;i++ )
#define REP_1(i,n) for(int i=1;i<=n;i++ )
#define FOR(i, a, b) for (int i=a;i<b;++i)
#define DWN(i, b, a) for (int i=b-1;i>=a;--i)
#define FOR_1(i, a, b) for (int i=a;i<=b;++i)
#define DWN_1(i, b, a) for (int i=b;i>=a;--i)
#define RST(A) memset(A, 0, sizeof(A))
#define FLC(A, x) memset(A, x, sizeof(A))

char str[N];

char fin[4005];

int main(){
    //freopen("in.txt","r",stdin);
	int t;
	scanf("%d",&t);
	
	int cas = 0;

	while(t--){
		cas++;
		printf("Case #%d: ",cas );
		scanf("%s",str);
		int n = strlen(str);
		
		int st = 1005;
		int ed = 1005;

		fin[st] = str[0];

		REP_1(i,n-1){

			if(str[i] >= fin[st]){
				st--;
				fin[st] = str[i];
			}
			else{
				ed++;
				fin[ed] = str[i];
			}
		}

		for(int i=st;i<=ed;i++){
			printf("%c",fin[i] );
		}
		puts("");
	}
    return 0;
}


















