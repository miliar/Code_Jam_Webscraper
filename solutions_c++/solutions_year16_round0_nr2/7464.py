/*--------------------------
|  Author- Advitiya Brijesh |
|  PIE @ MNNIT Allahabad    |
|  advitiyabrijesh@gmail.com|
|                           |
---------------------------*/
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<list<ll> > vli;
typedef vector<int> vi;
typedef vector<pair<ll,ll> > vpll;
typedef vector<pair<int,int> > vpii;
typedef pair<int ,int> pii;
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i=0;i<n;++i)
#define REP(i,a,b) for(int i=a;i<=b;++i)
#define PER(i,b) for(int i=b;i>=0;--i)
#define sd(n) scanf("%d",&n)
#define sld(n) scanf("%ld",&n)
#define sll(n) scanf("%lld",&n)
#define ss(n) scanf("%s",n)
#define sc(n) scanf("%c",&n)
#define oll(n) printf("%lld\n",n);
#define mset(n,k) memset(n,k,sizeof(n))
#define MOD 1000000007
#define MAX 2000005
#define MAXN 100005

int main(){
freopen("lucky.in","r",stdin);
    freopen("lucky.out","w",stdout);

    int t;
    sd(t);
    for(int tc=1;tc<=t;++tc){
        string s;
        cin>>s;
        int len=s.size();
        int cnt=1,pos=-1;
        for(int i=0;i<len;++i){
            if(s[i]=='-')
                pos=i;
        }
        if(pos==-1)
            cnt=0;
        else{
            for(int i=pos;i>0;--i){
                if(s[i]!=s[i-1])
                    cnt++;
            }
        }
        printf("Case #%d: %d\n",tc,cnt);
    }
return 0;}