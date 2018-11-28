/*when pink tuns blue*/

#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#include<cmath>
#include<ctime>

#define FO(i,s,e,p) for( int i=(s);i<int(e);i+=p)
#define FOD(i,s,e,p) for( int i=(s);i>int(e);i-=p)


#define FOR(i,s,e) FO(i,s,e,1)
#define FORE(i,s,e) FOR(i,s,e+1)
#define FORD(i,s,e) FOD(i,s,e,1)
#define FORDE(i,s,e) FORD(i,s,e-1)

#define ALL(i,s) for(__typeof((s).begin()) i=(s).begin();i!=(s).end();i++)

#define MEM(tab,fill) memset(tab,fill,sizeof(tab))

#include<iostream>
#include<set>
#include<vector>
#include<string>
#include<sstream>
#include<stack>
#include<queue>
#include<algorithm>
#include<utility>
#include<bitset>
#include<map>
#include<cassert>
#include<limits.h>
#define pb push_back


using namespace std;
#define EPS 0.0000001

#define mp make_pair
#define fi first
#define se second
#define inf ((1<<30)-1)
#define deb(a) cout<<#a<<' '<<a<<endl

#define llu unsigned ll

#define AL(a) (a).begin(),(a).end()

#define PI pair<int,int>
#define PII pair<PI,PI>

#define MIN(a,b) (((a)<(b))?(a):(b))



void solve(){
    set<int> ss;
    FORE(i,1,16) ss.insert(i);

    FOR(x,0,2){
    int a;cin>>a;
    FORE(i,1,4)
    FORE(j,1,4){
        int tmp;cin>>tmp;
        if(i!=a) ss.erase(tmp);
    }
    }
    if(ss.size()==0) cout<<"Volunteer cheated!";
    else if(ss.size()==1) cout<<*ss.begin();
    else cout<<"Bad magician!";

}



int main()
{
    freopen("C:\\a","r",stdin);
    freopen("C:\\w","w",stdout);
    int t;cin>>t;
    FORE(i,1,t){
        cout<<"Case #"<<i<<": ";
        solve();
        cout<<endl;
    }


    return 0;
}
