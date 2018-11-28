/*
prob: GCJ
id: i.amlansaha@gmail.com
lang: C++
date: 2016-04-30
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

int main ()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int i, j, k, l, temp, t, n, m, caseno = 0, ans;
    string str;
    int trck[257];
    scanf ( "%d", &t );
    map<char,int> mp;
    mp['Z']=0;
    mp['W']=2;
    mp['U']=4;
    mp['X']=6;
    mp['G']=8;
    mp['H']=3;
    mp['F']=5;
    mp['V']=7;
    mp['O']=1;
    mp['N']=9;
    string pref="ZWUXGHFVON";
    string num[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    while ( t-- )    {
        cin>>str;
        CLR(trck);
        string anss="";
        for(auto &x: str)   trck[x]++;
        FR(i,10)    {
            if(trck[pref[i]])   {
                k=mp[pref[i]];
                l=trck[pref[i]];
                if(k==9)    l/=2;
                for(auto &x: num[k])    trck[x]-=l;
                while(l--)  anss+=(char)(k+'0');

            }
        }
        sort(anss.begin(),anss.end());
        printf ( "Case #%d: ", ++caseno);
        cout<<anss<<endl;
    }
    return 0;
}
