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

int main(){ FI FO
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t;
    cin>>t;
    for(int cs=1;cs<=t;cs++){
        ll n,sum=0,cnt=0;
        string s;
        cin>>n;
        cin>>s;
        sum+=s[0]-'0';
        for(int i=1;i<s.length();i++){
            if(s[i]!='0'){
                if(sum<i){
                    cnt+=(i-sum);
                    sum+=(i-sum);
                    sum+=(s[i]-'0');
                }
                else{
                    sum+=(s[i]-'0');
                }
          }
        }
        cout<<"Case #"<<cs<<": "<<cnt<<endl;
    }
    return 0;
}

