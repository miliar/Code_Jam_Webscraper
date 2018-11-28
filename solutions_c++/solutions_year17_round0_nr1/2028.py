#include <bits/stdc++.h>
#include <tr1/unordered_map>
typedef long long ll;
typedef unsigned long long ull;
#define clr(ma) memset(ma,-1,sizeof ma)
#define inf 1000000000
#define vi vector<int>
#define pi pair<int  ,int >
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
#define mo(x) ((x)<P?(x):(x)-P)
#define mo2(x) ((x)>=0?(x):(x)+P)
#define fast ios_base::sync_with_stdio(0);cin.tie(0);
#define sc(s)  scanf("%s",s)
using namespace std;
char s [2000];
int n,k;
int main(){
    fi("/home/mohamedatef/ClionProjects/untitled1/input.txt");
    fo("/home/mohamedatef/ClionProjects/untitled1/out.txt");
    int t;
    in(t);
    for (int c=1;c<=t;c++){
        scanf("%s",s);in(k);
        int ans=0;
        n=strlen(s);
        for (int i=0;i<n;i++){
            if (s[i]=='+')continue;
            else{
                if (n-i>=k){
                    ans++;
                    for (int j=0;j<k;j++){
                        if (s[i+j]=='+')s[i+j]='-';
                        else s[i+j]='+';
                    }
                }
                else{
                    ans=-1;
                    break;
                }
            }
        }
        if (ans==-1)printf("Case #%d: IMPOSSIBLE\n",c);
        else printf("Case #%d: %d\n",c,ans);

    }
}