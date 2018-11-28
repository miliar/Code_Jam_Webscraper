#include<iostream>
#include<cstdio>
#include<algorithm>
#include<memory.h>
#include<vector>
#include<stack>
#include<queue>
#include<cassert>
#include<cstdlib>
#include<cmath>
#include<map>
#include<utility>
#include<cstring>

#define DEBUG(x) cout<<#x<<"= "<<x<<endl
#define DEBUGARR(x,i,f) for(int iter = i; iter <= f; ++iter) printf("%s[%d]=%d\n",#x, iter, x[iter])
#define MAX(a,b) ((a)>(b))? (a):(b)
#define MAX3(a,b,c) MAX(a,MAX(b,c))
#define MIN(a,b) ((a)<(b))? (a):(b)
#define MIN3(a,b,c) MIN(a,MIN(b,c))
#define bit(n,i) (n&(1<<(i-1)))
#define setbit(n,i) n |= (1<<(i-1))
#define inf (1<<30)
#define SETZERO(x) memset( x, 0, sizeof(x))
#define SETMIN1(x) memset( x, -1, sizeof(x))
#define CLEAR(x) while(!x.empty()) x.pop();
#define FOR(i,in,fin) for( i = (in); i <= (fin); ++i)
#define FORL(i,in,fin) for( i = (in); i < (fin); ++i)
#define FORD(i,in,fin) for( i = (in); i >= (fin); --i)
#define INC(a,b,c) ((a)<=(b) && (b)<=(c))
#define pb push_back
#define si(x) scanf("%d",&x)
#define pi(x) printf("%d\n",x)
#define sll(x) scanf("%lld",&x)
#define pll(x) printf("%lld\n",x)
#define sortv(v) sort(v.begin(),v.end())
#define sortar(a,i,n) sort(a+i,a+i+n)
#define findmp(mp,x) (mp.find(x)!=mp.end())
typedef long long ill;
using namespace std;
typedef pair <int,int> pii;
const int mod = 1000000007;
//code begins here
int main()
{
    #ifndef ONLINE_JUDGE
        freopen( "a.in", "r", stdin);
        freopen("a.out","w",stdout);
    #endif
    int t,test_case;
    scanf("%d",&t);
    FOR(test_case,1,t)
    {
        printf("Case #%d: ",test_case);
        int n;
        si(n);
        char a[101],b[101];
        vector <pair<char,int> > vc,vc1;
        scanf("%s%s",a,b);
        int i,cnt=1;
        char prev=a[0];
        for(i=1;a[i];++i){
            if(a[i]!=prev){
                vc.push_back(make_pair(prev,cnt));
                prev = a[i];
                cnt = 1;
            }
            else
                cnt++;
        }
        int ans=0;
        vc.push_back(make_pair(prev,cnt));
        prev = b[0],cnt=1;
        int j=0,flag=0;
        for(i=1;b[i];++i){
            if(b[i]!=prev){
                vc1.push_back(make_pair(prev,cnt));
                prev = b[i];
                cnt = 1;
            }
            else
                cnt++;
        }
        vc1.push_back(make_pair(prev,cnt));
        if(vc.size()==vc1.size()){
            FORL(i,0,vc.size()){
                if(vc[i].first!=vc1[i].first){
                    flag=1;
                    break;
                }
                else{
                    ans += abs(vc[i].second-vc1[i].second);
                }
            }
        }
        else{
            flag=1;
        }
        if(flag==0)
            pi(ans);
        else
            printf("Fegla Won\n");
    }
}


