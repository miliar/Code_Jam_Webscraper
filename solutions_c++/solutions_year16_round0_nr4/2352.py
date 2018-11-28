//By Tapesh Joham
#include<bits/stdc++.h>
using namespace std;

#define SCAN(x) scanf("%d",&x)
#define SCAN2(x,y) scanf("%d%d",&x,&y)
#define PRI(x) printf("%d\n",x)
#define FOR(A,B,C) for(int A=B;A<C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define MEM(A,B) memset(A,B,sizeof(A))
#define mod 1000000007
#define gc getchar_unlocked
typedef long long int LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<PII> VII;

int main()
{
    int test,k,c,s,cnt=0;
    SCAN(test);
    while(test--){
        cnt++;
        SCAN2(k,c);
        SCAN(s);
        printf("Case #%d: ",cnt);
        if(k==s){
            FOR(i,1,s+1)
                printf("%d ",i);
            printf("\n");
        }
        else puts("IMPOSSIBLE");
    }
	return 0;
}
