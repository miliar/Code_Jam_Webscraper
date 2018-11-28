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
void get(int i,vector<int>&v,int len )
{

    while(len--) {
        v.pb(i%2);
        i/=2;
    }
    v.pb(1);
    reverse(all(v));
    if(v.size()==0) v.pb(0);
    v.pb(1);
}

const long long MAX = 1e8;
bitset<MAX> b;

/*const int MAX = 1e6;
bitset<MAX> b;
*/
vector<int> Prime;

void seive()
{
    int sqn = sqrt(MAX);
    Prime.pb(2);
    for(int i= 3; i < MAX; i +=2 ) {
        if(b[i]==0) {
            Prime.pb(i);
            if(i > sqn ) continue;
            for(int j = i * i ; j < MAX; j += 2 * i) b[i]=1;
        }
    }
}
long long  isPrime(vector<int> &v, int base)
{
    for(int i=2 ; i < 1000; i ++ ) {
        long long sum = 0;
        for(int j = 0; j < v.size() ; j ++ ) {
            sum = base * sum + v[j];
            sum %= i;
        }
        if(sum == 0) return i;
    }

    return -1;
}
int main()
{
    freopen("out2.txt","w",stdout);
    //seive();
    //printf("SEIVE COMPLETE\n");
    int cnt = 0;
    printf("Case #%d:\n",1);
    int n = 32;
    for(int i = 0; i < (1<<(n-2)); i ++ ) {
        vector<int>v;
        vector<long long> yo;
        get(i,v,n-2);
        bool flag= 1;
        for(int base = 2 ; base <= 10; base ++ ) {

            long long uu = isPrime(v,base);
            if(uu < 0) {
                flag =0;
                break;
            }
            else {// printf("  Divides by %lld\n",uu);
                    yo.pb(uu);
            }
        }
        if(flag) {
            //printf("AN ANSWER\n");
            for(auto a: v) printf("%d",a);
            for(auto a: yo) printf(" %lld",a);
            printf("\n");
            cnt ++;
        }
        if(cnt==500) {
                //printf("DONE\n");
            break;
        }
    }

    return 0;
}
