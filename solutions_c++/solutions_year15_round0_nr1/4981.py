#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<numeric>
#include<fstream>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps (1e-9)
#define inf (1<<29)
#define i64 long long
#define u64 unsigned i64

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,i,total,ans,n,cs=1;
    string s;
    cin>>t;
    while(t--){
        cin>>n>>s;
        total = s[0] - '0';
        ans = 0;
        for(i = 1;i<=n;i++){
            if(total<i){
                ans+= i - total;
                total = i;
            }
            total+= s[i] - '0';
        }
        printf("Case #%d: %d\n",cs++,ans);
    }
	return 0;
}
