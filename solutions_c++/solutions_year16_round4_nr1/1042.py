#include<bits/stdc++.h>

using namespace std;

// Shortcuts for "common" data types in contests
typedef long long int ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
// To simplify repetitions/loops, Note: define your loop style and stick with it!
#define s(i) scanf("%d",&i)
#define sl(i) scanf("%ld",&i)
#define sll(i) scanf("%lld",&i)
#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define NREP(i,a,b) \
for (int i = int(a); i >= int(b); i--)
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 1000000000 // 2 billion
#define EPS 1e-9
#define MOD 1000000007

struct node{
    string val;
    int paper , rock , scissor ;
    node()
    {
        val = "";
        paper = rock = scissor = -1;
    }
};

node dp[3][13] ;

struct node memoize( int winner , int round )
{
    if( dp[winner][round].paper != -1 )
        return dp[winner][round];
    struct node ans , temp1 , temp2 ;
    if( winner == 0 )
    {
        temp1 = memoize( 0 , round - 1 );
        temp2 = memoize( 1 , round - 1 );
    }
    else if( winner == 1 )
    {
        temp1 = memoize( 1 , round - 1 );
        temp2 = memoize( 2 , round - 1 );
    }
    else if( winner == 2 )
    {
        temp1 = memoize( 2 , round - 1 );
        temp2 = memoize( 0 , round - 1 );
    }
    ans.paper = temp1.paper + temp2.paper;
    ans.rock  = temp1.rock + temp2.rock ;
    ans.scissor = temp1.scissor + temp2.scissor ;
    ans.val = min( temp1.val + temp2.val , temp2.val + temp1.val );
    return ans;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //freopen("input.in","r",stdin);
    //freopen("output.out","w",stdout);
    dp[0][0].val = "P";
    dp[0][0].paper = 1;
    dp[0][0].rock = 0;
    dp[0][0].scissor = 0 ;
    dp[1][0].val = "R";
    dp[1][0].paper = 0;
    dp[1][0].rock = 1;
    dp[1][0].scissor = 0 ;
    dp[2][0].val = "S";
    dp[2][0].paper = 0;
    dp[2][0].rock = 0;
    dp[2][0].scissor = 1;
    int t ;
    s(t) ;
    REP( T , 1 , t )
    {
        int n , rock , paper , scissor ;
        s(n) ; s(rock) ; s(paper) ; s(scissor) ;
        string res = "IMPOSSIBLE" ;
        REP( i , 0 , 2 )
        {
            struct node ans = memoize( i , n );
            if( ans.rock == rock && ans.paper == paper && ans.scissor == scissor )
            {
                if( res == "IMPOSSIBLE" )
                    res = ans.val;
                else
                    res = min( res , ans.val );
            }
        }
        cout << "CASE #" << T << ": " << res << endl;
    }
    return 0;
}
