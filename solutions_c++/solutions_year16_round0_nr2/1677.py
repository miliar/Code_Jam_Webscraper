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
#define INF 2000000000 // 2 billion
#define EPS 1e-9
#define MOD 1000000007

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //freopen("input.in","r",stdin);
    //freopen("output.out","w",stdout);
    int t ; s(t) ;
    REP( T , 1 , t )
    {
        string str;
        cin >> str;
        int len = str.length() , ans =  0 ;
        NREP( i , len - 1 , 0 )
        {
            if( str[i] == '-' )
            {
                ans++;
                REP( j , 0 , i )
                {
                    if( str[j] == '-' )
                        str[j] = '+';
                    else
                        str[j] = '-';
                }
            }
        }
        printf("Case #%d: %d\n",T,ans);
    }
    return 0;
}
