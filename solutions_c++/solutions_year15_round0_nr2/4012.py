#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long long LL;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#ifdef DEBUG
    #define cek(x) cout<<x
#else
    #define cek(x) if(false){}
#endif // DEBUG

#define fi first
#define se second
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define EPS 1e-9
#define PI acos(-1.0)
#define pb push_back
#define TC() while(tc--)
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORN(i,n) for(int i=0;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define REPN(i,a,b) for(int i=a;i<=b;i++)
#define reset(a,b) memset(a,b,sizeof(a))
#define sc(x) scanf("%d",&x)

int rec(int arr[], int now, int tot){
    if(now == 1){
        return tot + now;
    }
    int smallest = now + tot;

    if(arr[now]>0){
        //printf("%d %d\n",now,tot);
        if(now == 9){
            int temp = arr[now];
            arr[3] += arr[now]*3;
            arr[now] = 0;

            smallest = min(smallest, rec(arr, 8, tot+temp*2));
            arr[3]-=temp*3;
            arr[now] = temp;
            arr[5]+=temp;
            arr[4]+=temp;
            smallest = min(smallest, rec(arr, 8, tot+temp));
            arr[5]-=temp;
            arr[4]-=temp;
        }else{
            arr[now/2]+=arr[now];
            arr[(now+1)/2]+=arr[now];
            smallest = min(smallest, rec(arr, now - 1, tot + arr[now]));
        }
    }else{
        smallest = min(smallest, rec(arr, now-1, tot));
    }
    return smallest;
}

int main(void){
    #ifdef ccsnoopy
        freopen("C:/Users/SONY/Desktop/B-small-attempt4.in","r",stdin);
        freopen("C:/Users/SONY/Desktop/out.txt","w",stdout);
    #endif
    //to compile: g++ -o foo filename.cpp -lm -Dccsnoopy for debug.
    int tc;
    sc(tc);
    int arr[1010];
    int casecounter = 1;
    while(tc--){
        int n,x, maxi;
        maxi = 0;
        sc(n);
        reset(arr,0);
        FOR(i,n){
            sc(x);
            arr[x]++;
            maxi = max(x,maxi);
        }
        printf("Case #%d: %d\n",casecounter++, rec(arr, 9, 0));
    }

    return 0;
}



