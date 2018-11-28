/* Code Jam Template */
#include <bits/stdc++.h>
using namespace std;
#define MOD 					1000000007
#define pb(x) 					push_back(x)
#define mp(x,y)                 make_pair(x,y)
#define FF 						first
#define SS 						second
#define s(n) 					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define ss(n) 					scanf("%s",n)
//special macro for reading a character of input
#define sc(n)                   {char temp[4]; ss(temp); n=temp[0];}
#define INF						(int)1e9
#define LINF					(long long)1e18
#define EPS						1e-9
/*
Use these macros when comparing variables of different data types.
For e.g. comparing int and long long will give error when used with std::max, use maX instead.
*/
#define maX(a,b)				((a)>(b)?(a):(b))
#define miN(a,b)				((a)<(b)?(a):(b))
#define abS(x)					((x)<0?-(x):(x))
typedef long long ll;
typedef unsigned long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef pair<int,PII> TRI;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<ll> vl;
typedef vector<PII> VII;
typedef vector<TRI> VT;

/*Main code begins now*/

void precompute() {
    /*
    Code that is common to all test cases and should be run before solving for any case, like Prime-NUmber Generation :)
    */


}
int d,p[1004];
priority_queue <int> pq;
void read() {
    /*
    Read Global variables here
    */
    cin>>d;
    int x;
    memset(p,0,sizeof(p));
    for(int i=0;i<d;i++) {
        cin>>p[i];
    }

}

bool func(int arr[100],int time,int n)
{
    int max=arr[0],pos=0,i;
    for(i=0;i<n;i++) {
        if(arr[i]>max) {max=arr[i];
        pos=i;
        }
    }
    if(max<=3)
    {
        if(time>=max) {
               // for(i=0;i<n;i++) cout<<arr[i];
               // cout<<time<<endl;
               return true;}
        else return false;
    }
    if(time==1) return false;
    if(time>=max) return true;
    for(i=2;i<=max-i;i++)
    {
        arr[pos]=i;
        arr[n]=max-i;
        if(func(arr,time-1,n+1)) return true;

    }
    arr[pos]=max;
    return false;
}

void solve() {

    /*
    Main logic goes here
    */

    int j,i,arr[100];
     sort(p,p+d);
    for(i=1;i<=9;i++)
    {
       for(j=0;j<d;j++) arr[j]=p[j];
       if(func(arr,i,d)) break;

    }
    cout<<i<<endl;
}

int main(){
   freopen("B.in", "r", stdin);
	freopen("output.in", "w", stdout);
	precompute();
	//cout<<primecount[1];
	//cout<<cat[2];
	int t;
	s(t);

	for(int T = 1; T <= t; T++) {
	    read();
	    printf("Case #%d: ",T);
        solve();
  	}
	return 0;
}
