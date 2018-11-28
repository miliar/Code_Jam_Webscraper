/*
 * Bidhan Roy
 * University of Dhaka
 */

using namespace std;

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <ctime>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define rep(i,n) for(__typeof(n) i=0; i<(n); i++)
#define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)
#define inf (1<<30)
#define eps 1e-9
#define pb push_back
#define ins insert
#define mp make_pair
#define sz(x) ((int)x.size())
#define clr clear()
#define all(x) x.begin(),x.end()
#define xx first
#define yy second
#define sqr(x) ((x)*(x))
#define mem(x,val) memset((x),(val),sizeof(x));
#define read(x) freopen(x,"r",stdin);
#define rite(x) freopen(x,"w",stdout);

typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef map<int,st> mis;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

#define mx 0

char num[20];

bool pal(i64 n){
    sprintf(num,"%lld",n);
    int len=strlen(num);
    for(int i=0; num[i]; i++){
        if(num[i]!=num[len-i-1]) return false;
    }
    return true;
}

vector<i64> ans;

int main(){
    read("cin.txt");
    rite("cout.txt");
    for(i64 i=1; i<=10000010LL; i++){
        if(pal(i) && pal(i64(i)*i64(i))) ans.pb(i64(i)*i64(i));
    }
    sort(all(ans));
    int test,kas=0;
    cin>>test;
    while(test--){
        i64 a,b;
        scanf("%lld%lld",&a,&b);
        i64 res=(upper_bound(all(ans),b)-ans.begin())-1;
        a--;
        b=a;
        res-=(upper_bound(all(ans),b)-ans.begin())-1;
        printf("Case #%d: %lld\n",++kas,res);
    }
    return 0;
}
