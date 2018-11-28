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
string s;
vector<int>v;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cs=0;
    cin >> t;
    while(t--) {
        cin >> s;
        for(int i= 0;i < s.length(); i ++ ) {
            if(s[i]=='+') v.pb(1);
            else v.pb(0);
        }
        int ans = 0;
        while(v.size()){
            while(v.size() && v.back() == 1) v.pop_back();
            //for(auto a: v) printf("%d",a);puts("");
            if(v.size() && v.back() ==0 && v[0]== 0) {
                reverse(all(v));
                for(int i=0;i<v.size();i++) v[i]^=1;
                ans ++;
            }
            if(v.size() && v.back() == 0 && v[0]==1) {
                int i = 0;
                while(i<v.size() && v[i]==1) i ++;
                reverse(v.begin(), v.begin() + i);
                for(int k = 0; k < i; k ++ ) v[k] ^=1;
                ans ++;
            }
            //for(auto a: v) printf("%d",a);puts("");
            //printf("ANS -> %d\n",ans);
        }
        printf("Case #%d: %d\n",++cs,ans);
        v.clear();
    }
    return 0;
}
