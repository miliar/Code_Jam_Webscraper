#include<string>
#include<iostream>
#include <map>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<set>
#include<bitset>
#include<utility>
#include<cstring>
#include<climits>
#include<cassert>
// I'M FUCKING lazy :)
using namespace std;
#define LL long long int
#define mfor(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORL(i,a,b) for(long long int i=a;i<=b;i++)
#define RFOR(i,a,b) for(int i=a;i>=b;i--)
#define SND(x) scanf("%d",&x)
#define PTD(x) printf("%d\n",x)
#define SNLL(x) scanf("%lld",&x)
#define PTLL(x) printf("%lld\n",x)
#define PTS() printf("\n");
#define OPEN freopen("in.txt","r",stdin)
#define WRITE freopen("out.txt","w",stdout)
#define pb push_back
#define mp make_pair
#define IS_ODD( num ) ((num) & 1)
#define IS_EVEN( num ) (!IS_ODD( (num) ))
#define MEM(dest,val) memset(dest,val,sizeof(dest))
typedef pair<int,int>ii;
typedef vector<int>vi;
typedef vector<ii>vii;
int tc,ans,no,n;
string s;
int main(){
    OPEN;
    WRITE;
    SND(tc);
    FOR(j,1,tc){
        cin>>n>>s;ans=no=0;
        FOR(i,0,n){
            if((s[i]-'0')>0)if(i>(no+ans))ans+=i-(no+ans);//cout<<i<<"       "<<no;}
            //cout<<s[i]-'0'<<"     "<<ans<<endl;
            no+=s[i]-'0';
        }
        printf("Case #%d: %d\n",j,ans);
    }

    return 0;
}
