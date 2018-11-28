/*
 *************************
 Id  : Matrix.code
 Task:
 Date: 2016-04-30

 **************************
 */

#include<bits/stdc++.h>
using namespace std;
/*------- Constants---- */

#define Long                    long long
#define Ulong                   unsigned long long
#define forn(i,n)               for( int i=0 ; i < n ; i++ )
#define mp(i,j)                 make_pair(i,j)
#define pb(a)                   push_back((a))
#define SZ(a)                   (int) a.size()
#define all(x)                  (x).begin(),(x).end()
#define gc                      getchar_unlocked
#define PI                      acos(-1.0)
#define EPS                     1e-9
#define xx                      first
#define yy                      second
#define lc                      ((n)<<1)
#define rc                      ((n)<<1|1)
#define db(x)                   cout << #x << " -> " << x << endl;
#define Di(x)                   int x;scanf("%d",&x)
#define min(a,b)                ((a)>(b) ? (b) : (a) )
#define max(a,b)                ((a)>(b) ? (a):(b))
#define ms(ara_name,value)      memset(ara_name,value,sizeof(ara_name))

/*************************** END OF TEMPLATE ****************************/

const int N = 1001;

string dig[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
char str[20004];
int cnt[150];
int ans[11];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cs=0;
    scanf("%d",&t);
    while(t--) {
        scanf("%s",str);
        int len = strlen(str);
        memset(cnt,0,sizeof cnt);
        for(int i = 0; i < len; i ++) {
            cnt[str[i]] ++;
        }
        while(cnt['Z'] > 0) {
            ans[0] ++;
            for(int i= 0;i < dig[0].size(); i ++ ) {
                cnt[dig[0][i]] --;
            }
        }
        while(cnt['W'] > 0) {
            ans[2] ++;
            for(int i= 0;i < dig[2].size(); i ++ ) {
                cnt[dig[2][i]] --;
            }
        }
        while(cnt['U'] > 0) {
            ans[4] ++;
            for(int i= 0;i < dig[4].size(); i ++ ) {
                cnt[dig[4][i]] --;
            }
        }
        while(cnt['F'] > 0) {
            ans[5] ++;
            for(int i= 0;i < dig[5].size(); i ++ ) {
                cnt[dig[5][i]] --;
            }
        }
        while(cnt['X'] > 0) {
            ans[6] ++;
            for(int i= 0;i < dig[6].size(); i ++ ) {
                cnt[dig[6][i]] --;
            }
        }
        while(cnt['G'] > 0) {
            ans[8] ++;
            for(int i= 0;i < dig[8].size(); i ++ ) {
                cnt[dig[8][i]] --;
            }
        }
        while(cnt['S'] > 0) {
            ans[7] ++;
            for(int i= 0;i < dig[7].size(); i ++ ) {
                cnt[dig[7][i]] --;
            }
        }
        while(cnt['R'] > 0) {
            ans[3] ++;
            for(int i= 0;i < dig[3].size(); i ++ ) {
                cnt[dig[3][i]] --;
            }
        }
        while(cnt['O'] > 0) {
            ans[1] ++;
            for(int i= 0;i < dig[1].size(); i ++ ) {
                cnt[dig[1][i]] --;
            }
        }
        while(cnt['I'] > 0) {
            ans[9] ++;
            for(int i= 0;i < dig[9].size(); i ++ ) {
                cnt[dig[9][i]] --;
            }
        }
        printf("Case #%d: ",++cs);
        for(int i = 0; i < 10; i ++) {
            for(int j = 0; j < ans[i]; j ++) printf("%d",i);
        }
        printf("\n");
        ms(ans,0);
        ms(cnt,0);
    }
}
