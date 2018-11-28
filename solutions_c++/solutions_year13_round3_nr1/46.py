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
#define chk(a,k) ((bool)(a&(1<<(k))))
#define off(a,k) (a&(~(1<<(k))))
#define on(a,k) (a|(1<<(k)))

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
typedef pair<i64,i64> pii;
typedef vector<pii> vpii;

#define mx 2000000

char name[mx];

int vow(char ch){
    if(ch=='a') return 1;
    if(ch=='e') return 1;
    if(ch=='i') return 1;
    if(ch=='o') return 1;
    if(ch=='u') return 1;
    return 0;
}

int Next[mx];
int dp[mx];

int main(){
	double cl = clock();
    cl = clock() - cl;
    read("ALarge.in");
    rite("AoutLarge.txt");
    int test,kas=0;
    cin>>test;
    while(test--){
        printf("Case #%d: ",++kas);
        int n;
        cin>>name>>n;
        i64 ans=0;
        int len=strlen(name);
        int id=-1;
        mem(Next,-1);
        int wh=-1;
        for(int i=len-1; i>=0; i--){
            if(vow(name[i])) id=-1;
            else{
                if(id==-1) id=i;
                Next[i]=id;
                if(Next[i]-i+1>=n) wh=i;
            }
            dp[i]=wh;
            //cout<<Next[i]<<endl;
        }
        //rep(i,len) cout<<i<<"="<<dp[i]<<endl;
        int i=0;
        while(i<len){
            if(dp[i]!=-1){
                int j=dp[i]+n-1;
                ans+=len-j;
            }
            i++;
        }
        cout<<ans<<endl;
    }
    fprintf(stderr, "Total Execution Time = %lf seconds", cl / CLOCKS_PER_SEC);
    return 0;
}
