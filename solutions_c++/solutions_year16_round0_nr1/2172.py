/*
 *************************
 Id  : Matrix.code
 Task:
 Date: 2016-04-09

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
bool vis[10];
int main()
{
    /*
    freopen("in.txt","w",stdout);
    for(int i= 1; i <= 1000000; i ++) {
        long long temp = 0;
        int cnt = 0;
        ms(vis,0);
        while(1){
            temp  += i;
            long long t = temp;
            while(t){
                if(vis[t%10] == 0) cnt++;
                if(cnt==10) break;
                vis[t%10] = 1;
                t/=10;
            }
            if(cnt == 10) break;
        }
        printf("%d -> %lld\n", i, temp);
    }*/


    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int t,cs=0;
    cin >> t;
    while(t--) {
        long long n;
        scanf("%d",&n);
        if(n==0) printf("Case #%d: INSOMNIA\n",++cs);
        else {
            long long temp = 0;
            int cnt = 0;
            ms(vis,0);
            while(1){
                temp  += n;
                long long t = temp;
                while(t){
                    if(vis[t%10] == 0) cnt++;
                    if(cnt==10) break;
                    vis[t%10] = 1;
                    t/=10;
                }
                if(cnt == 10) break;
            }
            printf("Case #%d: %lld\n",++cs,temp);

        }
    }

    return 0;
}
