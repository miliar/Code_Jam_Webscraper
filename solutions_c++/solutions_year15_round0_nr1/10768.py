
#include <iostream>
#include <fstream>
#include <string.h>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <cassert>
#include <list>
#include <iomanip>
#include <math.h>
#include <deque>
#include <utility>
#include <map>
#include <set>
#include <bitset>
#include <numeric>
#include <climits>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <sstream>

#define  MOD 1000000007
#define rep(i,n) for(int i = 0; i < n; ++i)
#define rrep(i,n) for(int i = 1; i <= n; ++i)
#define drep(i,n) for(int i = n-1; i >= 0; --i)
#define gep(i,g,j) for(int i = g.head[j]; i != -1; i = g.e[i].next)
#define each(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rng(a) a.begin(),a.end()
#define maxs(x,y) x = max(x,y)
#define mins(x,y) x = min(x,y)
#define pb push_back
#define sz(x) (int)(x).size()
/*vi s;
 cout<<sz(s);
 sort(s.begin(), s.end(), myfunction);*/
#define  MOD 1000000007
#define rep(i,n) for(int i = 0; i < n; ++i)
#define rrep(i,n) for(int i = 1; i <= n; ++i)
#define drep(i,n) for(int i = n-1; i >= 0; --i)
#define gep(i,g,j) for(int i = g.head[j]; i != -1; i = g.e[i].next)
#define each(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rng(a) a.begin(),a.end()
#define maxs(x,y) x = max(x,y)
#define mins(x,y) x = min(x,y)
#define pb push_back
#define sz(x) (int)(x).size()
#ifndef ONLINE_JUDGE
#define gc getchar
#define pc putchar
#else
#define gc getchar_unlocked
#define pc putchar_unlocked
#endif
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long int  ll;
typedef pair<int, int> pii;
bool myfunction (int i,int j) { return (i<j); }
typedef std::pair<int,int> mypair;
bool comparator ( const mypair& l, const mypair& r)
{ return l.first < r.first; }
typedef long long int  ll;
long long int gcd ( long long int a,long long int b )
{
    long long  int c;
    while ( a != 0 ) {
        c = a; a = b%a;  b = c;
    }
    return b;
}
long long int lcm(long long int a,long long int b)
{
    return (a*b)/gcd(a,b);
}
long long int fact (int n ){
    if (n==1||n==0) {
        return 1;
    }
    else return n*fact(n-1);
    
}
typedef long long int  ll;




struct liste {
    int num;
    struct liste *suivant;
};

int sol=0,ta[5];
void con(int deep,string s){
    if (deep==0) {
        int y=1;
        for (int i =0; i<6; i++) {
            ta[i]=0;
        }
        
        
        for (int i =0; i<s.length(); i++) {
            ta[s[i]-'0']++;
            if (s[i]==s[i+1]) {
                y=0;
            }
        }
        sol+=y;
        
        
        if(y){ cout<<s<<"       "<<y<<"\n";
            for (int i =1; i<5; i++) {
                cout<<ta[i]<<" ";
            }
            cout<<"\n";
        
        
        }
        return;
    }
    for (int i ='1'; i<='4'; i++) {
        string d=" ";
        d=s;
        d+=i;
        con(deep-1,d);
        d=s;
        
    }

}


int main()
{
    ios::sync_with_stdio(false);
    ll t;
    cin>>t;
 
    for (int m =0; m<t; m++) {
        ll s;
        cin>>s;
        ll t[s+1];
        ll sol[s+1];
        int solu=0;
        string temp;
        cin>>temp;
        for (int i =0; i<s+1; i++) {
            t[i]=temp[i]-'0';
        }
        
        
        
        
        for (int i =0; i<s+1; i++) {
            sol[i]=0;
            if(i>0)sol[i]=t[i]+sol[i-1];
            else sol[i]=t[i];
            if (i>sol[i-1]+solu) {
                solu=(i-sol[i-1]);
            }
        }
        cout<<"Case #"<<m+1<<": "<<solu<<"\n";
        
    }
    
    
   
    
    return 0;
}