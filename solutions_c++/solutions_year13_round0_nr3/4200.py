
/*
 * Amit Mandal
 * Computer Science & Engineering
 * University of Dhaka
 */


#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<string>
#include<set>
#include<bitset>

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

#define INF (1<<30)
#define EPS 1e-9
#define PI acos(-1.0)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(a) ((a)<0?(-(a)):(a))
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define BIG(a) memset(a,63,sizeof(a))
#define SZ(a) ((int)a.size())
#define PB push_back
#define ALL(a) a.begin(),a.end()
#define ff first
#define ss second
#define MP make_pair

#define SF(a)  scanf("%lld",&a)
#define PF printf
#define NL puts("")


using namespace std;
typedef long long int LL;
#define mx 100000000000009
vector<LL> isp;

inline bool check(LL i){
    LL num=i, n=i,rev=0,dig;
    while(n != 0){
        dig=n%10;
        rev=rev*10 + dig;
        n/=10;
    }
    if(num == rev) return true;
    return false;
}

void process(){
    LL lim = (LL)sqrt(mx);
    lim++;
    for(LL i=1; i<=lim;i++){
        if(check(i)){
            LL fs=i*i;
                if(fs<mx)
                    if(check(fs))
                        isp.PB(fs);
        }
    }
}

int main()
{
    //READ("C-large-1.in");
    //WRITE("CLARGEout.in");
    process();
    LL arr[1000];
    int cnt=0;
    for(int i=0; i<SZ(isp); i++)  arr[cnt++]=isp[i];
    LL t;
    SF(t);
    int kase=1;
    while(t--){
        LL a,b;
        SF(a); SF(b);
        LL res=upper_bound(arr,arr+cnt,b)-arr;
        LL res2 = upper_bound(arr,arr+cnt,a-1)-arr;
        printf("Case #%d: %lld\n",kase++,res-res2);
    }
    return 0;
}

