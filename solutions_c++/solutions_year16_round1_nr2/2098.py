/*
prob: Codejam2016 -
id: amlan
lang: C++
date: 2016-04-16
algo:
*/
#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long LLU;
typedef vector<int> VI;
typedef vector<long long> VLL;
typedef map<int, int> MAPII;
typedef map<string,int> MAPSI;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;
typedef pair<double, double> PDD;

#define FOR(i,a,b) for(i=a;i<=b;i++)
#define ROF(i,a,b) for(i=a;i>=b;i--)
#define FR(i,n)    for(i=0;i<n;i++)
#define RF(i,n) for(i=n;i>0;i--)
#define CLR(a) memset ( a, 0, sizeof ( a ) )
#define RESET(a) memset ( a, -1, sizeof ( a ) )
#define PB(a)    push_back ( a )
#define X first
#define Y second

const int INF = 2000000009;
const int Max = 1000007;
const double PI = acos(-1.0);

int trck[3000];

int main ()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int i, j, k, l, temp, t, n, m, caseno = 0, ans;
    string str;
    scanf ( "%d", &t );
    VI anss;

    while ( t-- )    {
        cin>>n;
        CLR(trck);
        FR(i,(2*n-1)) {
            FR(j,n) {
                cin>>temp;
                trck[temp]+=1;
            }
        }
        anss.clear();
        FR(i,3000) {
            if(trck[i]%2)   anss.PB(i);
        }
        sort(anss.begin(),anss.end());
        printf ( "Case #%d:", ++caseno);
        l = anss.size();
        FR(i,l) {
            printf(" %d",anss[i]);
        }
        cout<<endl;
    }
    return 0;
}
