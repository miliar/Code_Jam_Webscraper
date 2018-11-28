#include <cstdio>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <climits>
#include <utility>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <cmath>
#define REP(i,n) for( int (i)=0;(i)<(int)(n);(i)++)
#define REPIT(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
LL LLMAX = 9223372036854775807LL;
const int MOD = 1000000007;
const int maxn = 1000+10;
bool pal(LL x){
    char str[100];
    sprintf(str,"%lld",x);
    int len = strlen(str);
    int n = len/2;
    for(int i=0;i<=n;++i)if(str[i]!=str[len-i-1])return false;
    return true;
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("C-large-1.in","r",stdin);
	freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(false);
    vector<LL> S;

    for(LL i=1;i<=10000001;++i)
        if(pal(i)&&pal(i*i))S.push_back(i*i);
    //for(int i=0;i<10;++i)cout<<S[i]<<endl;

    int T;
    LL a,b;
    cin>>T;
    for(int kase=1;kase<=T;++kase){
        cin>>a>>b;
        LL x = lower_bound(S.begin(),S.end(),a) - S.begin();
        LL y = upper_bound(S.begin(),S.end(),b) - S.begin();
        cout<<"Case #"<<kase<<": "<<y-x<<endl;
    }
}
