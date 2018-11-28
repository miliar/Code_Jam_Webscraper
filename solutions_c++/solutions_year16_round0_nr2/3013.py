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

char inverse(char n)
{
    if(n=='+')
        return '-';
    return '+';
}

int main()
{
	int test,cnt=0;
	SCAN(test);
	while(test--){
        cnt++;
        string x;
        cin >> x;
        int len = x.length();
        printf("Case #%d: ",cnt);
        int ans=0;
        RFOR(i,len-1,0){
            if(x[i]=='-'){
                ans++;
                RFOR(j,i,0)
                    x[j]=inverse(x[j]);
            }
        }
        PRI(ans);
	}
	return 0;
}
