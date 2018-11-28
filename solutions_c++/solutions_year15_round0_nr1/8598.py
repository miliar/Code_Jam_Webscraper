/*
    User: garyclay08
    Prog:
    Langauge: C++
*/

// Header File 

#include <bits/stdc++.h>

using namespace std;

// Input macros

#define si(n)                       scanf("%d",&n)
#define sc(n)                       scanf("%c",&n)
#define sl(n)                       scanf("%lld",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)
 
// Useful constants

#define INF                         (int)1e9
#define EPS                         1e-9
#define MOD1                        1000000009
#define MOD2                        1000000007

// Useful hardware instructions

#define bitcount                    __builtin_popcount
#define gcd                         __gcd
 
// Useful container manipulation / traversal macros

#define forI(i,n)                   for(i=0  ; i< n ;i++)
#define forD(i,n)                   for(i=n-1; i>=0 ;i--)  
#define forall(i,a,b)               for(i=a  ; i<=b ;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair
 
// Some common useful functions

#define MAX(a,b)                     ( (a) > (b) ? (a) : (b))
#define MIN(a,b)                     ( (a) < (b) ? (a) : (b))
#define checkbit(n,b)                ( (n >> b) & 1)
#define DREP(a)                      sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)               (lower_bound(all(arr),ind)-arr.begin())
 
// datatypes

#define ll                           long long int
#define ull                          unsigned long long
#define ui                           unsigned int
#define us                           unsigned short
#define vi                           vector<int>
#define pii                          pair<int,int>
#define gc                           getchar_unlocked
#define pc                           putchar_unlocked 

// Faster Input/Output

inline void get_int(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

inline void get_long(ll &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}
inline void print_int(int X)
{
    if(X<0) { pc('-');  X=-X;  }
    int Len=0,Data[20];
    while(X) { Data[Len++]=X%10; X/=10; }
    if(!Len) Data[Len++]=0;
    while(Len--) pc(Data[Len]+48);
    pc('\n');
}
inline void print_long(long long int X)
{
    if(X<0) { pc('-');  X=-X;  }
    int Len=0,Data[20];
    while(X) { Data[Len++]=X%10; X/=10; }
    if(!Len) Data[Len++]=0;
    while(Len--) pc(Data[Len]+48);
    pc('\n');
}

// Main Function

int main()
{
    //ios_base::sync_with_stdio(false);
    ll t,n,test;
    get_long(test);
    forall(t,1,test)
    {
        get_long(n);
        char s[n+10];
        ss(s);
        ll i,sum,c,x;
        sum=c=0;
        forI(i,n+1)
        {
            x=s[i]-'0';
            if(sum<i)
            {
                c+=(i-sum);
                sum+=(i-sum);
            }
            sum+=x; 
        }
        printf("Case #%lld: %lld\n",t,c);
    }
    return 0;
}