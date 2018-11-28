/*******************
  	Rahul Bhati
	CHARUSAT UNIVERSITY
	***********************/

#include <bits/stdc++.h>

using namespace std;

/* Time saving techniques :D */

typedef long long ll;
typedef unsigned long long ull;
typedef vector <int> vi;
typedef pair< int ,int > pii;
typedef istringstream iss;
typedef ostringstream oss;

#define pb              push_back
#define mp              make_pair
#define ff              first
#define ss              second
#define sz              size()
#define ln              length()
#define rep(i,n)        for(int i=0;i<n;i++)
#define fu(i,a,n)       for(int i=a;i<=n;i++)
#define fd(i,n,a)       for(int i=n;i>=a;i--)
#define foreach(it,v)   for( __typeof((v).begin())it = (v).begin() ; it != (v).end() ; it++ )
#define all(a)          a.begin(),a.end()
#define INF             (int)1e9
#define EPS             (1e-9)
#define INF_MAX         2147483647
#define INF_MIN         -2147483647
#define pi              acos(-1.0)
#define N               1000000
#define si(n)           scanf("%d",&n)
#define sll(n)          scanf("%lld",&n)
#define dbg(x)          { cout<< #x << ": " << (x) << endl; }
#define dbg2(x,y)       { cout<< #x << ": " << (x) << " , " << #y << ": " << (y) << endl; }
#define mset(a, s)      memset(a, s, sizeof (a))
#define FI              freopen("in.txt", "r", stdin);
#define FO              freopen("out.txt", "w", stdout);

int arr[1003];

int main(){ FI FO
    int t,d,i,j,mxsec,mnsec,sum,step=0;
    scanf("%d",&t);
    while(t--){
        scanf("%d", &d) ;
        for(i=0;i<d;i++){
            scanf("%d", &arr[i]) ;
            mxsec = max(mxsec,arr[i]) ;
        }

        mnsec = mxsec ;
        for(i=1;i<=mxsec;i++){
            sum=i;
            for(j=0;j<d;j++){
                if( arr[j] > i ){
                    if( arr[j]%i == 0 )
                        sum += (arr[j]/i-1) ;
                    else
                        sum += (arr[j]/i) ;
                }
            }
            mnsec = min(mnsec,sum) ;
        }
        printf("Case #%d: %d\n", ++step, mnsec) ;
    }
    return 0 ;
}
