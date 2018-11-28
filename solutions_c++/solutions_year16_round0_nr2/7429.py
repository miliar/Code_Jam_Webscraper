/*
Ahmed Dinar
CSE,JUST
*/
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<deque>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
#include<limits>

using namespace std;

#define FI           freopen("B-large.in","r",stdin)
#define FO           freopen("out.txt","w",stdout)

#define MS(x,v)      memset(&x,v,sizeof(x))
#define CL(x)        memset(&x,0,sizeof(x))
#define mp           make_pair
#define pb           push_back
#define ss           second
#define fi           first

#define vanish       scanf("\n")
#define nl           puts("")
#define endl         '\n'
#define i64          long long
#define all(x)       x.begin(),x.end()

#define Iterate(s)   for(typeof(s.begin()) it = s.begin(); it != s.end(); it++)
#define FOR(i,k,n)   for(__typeof(n) i = (k); i <= (n); ++i)
#define For(i,k,n)   for(__typeof(n) i = (k); i < (n); ++i)
#define ROF(i,k,n)   for(__typeof(n) i = k; i >= n; i--)
#define REP(i,n)     for(__typeof(n) i = 0; i < (n); ++i)
#define sq(x)        ((x)*(x))

#define PI           acos(-1.0)
#define EPS          0.0000001
#define MOD          1000000007

#define oo           100000000000000LL
#define MAX          105

char s[MAX];

int main(){

   // FI;
   // FO;


    int t,T=0;
    scanf("%d",&t);
    while(t--){
        scanf("%s",&s);

        int len = strlen(s);
        int flip = 0;
        int ans = 0;

        for(int i=len-1; i>=0; i--){
            if( s[i] == '-' && flip == 0 ){
                ans++;
                flip = 1;
            }
            else if( s[i] == '+' && flip == 1 ){
                flip = 0;
                ans++;
            }
        }


        printf("Case #%d: %d\n",++T,ans);
    }
    return 0;
}
