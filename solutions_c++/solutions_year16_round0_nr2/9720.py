#include <bits/stdc++.h>
#include <tr1/unordered_map>
typedef long long ll;
typedef unsigned long long ull;
#define clr(ma) memset(ma,-1,sizeof ma)
#define inf 30000000;
#define vi vector<int>
#define pi pair<int,int>
#define T2 pair<pi ,pi >
#define mk make_pair
#define getBit(m,i) ((m&(1<<i))==(1<<i))
#define setBit(m,i) (m|(1<<i))
#define setBit2(m,i) (m|(1ull<<i))
#define cont(i,ma) ((ma.find(i))!=(ma.end()))
#define in(i) scanf("%d",&i)
#define in2(i,j) scanf("%d%d",&i,&j)
#define in3(i,j,k) scanf("%d%d%d",&i,&j,&k)
#define in4(i,j,k,l) scanf("%d%d%d%d",&i,&j,&k,&l)
#define il(i) scanf("%I64d",&i)
#define itr map<ll,ll>::iterator
#define itr2 map<ll,map<ll,ll> >::iterator
#define id(k) scanf("%9lf",&k)
#define fi(ss) freopen (ss,"r",stdin)
#define fo(ss) freopen (ss,"w",stdout)
#define clean(vis)  memset(vis,0,sizeof vis)
using namespace std;
int main(){
	fi("B-large.in");
    fo("badryy.txt");
    char s [100+5];
    int t;
    in(t);
    int cnt=1;
    while (t--) {
        scanf("%s", s);
        int n=strlen(s);
        ll  ans=0;
        for (int i=n-1;i>=0;i--){
            if (s[i]=='+')continue;
            ans++;
            for (int j=i-1;j>=0;j--)if (s[j]=='+')s[j]='-';else s[j]='+';
        }
        cout<<"Case #"<<cnt++<<": "<<ans<<"\n";
    }


}
