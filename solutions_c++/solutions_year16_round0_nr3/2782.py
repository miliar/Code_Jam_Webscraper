#include<bits/stdc++.h>
using namespace std;
int arrr[1000005];
#define ll long long int
#define VI vector<int>
#define VLL vector<long long int>
#define PQI priority_queue<int>
#define PQLL priority_queue<long long int>
#define VP vector<pair<int,int> >
#define II pair<int,int> 
#define ll long long int
#define mem(in,val) memset(in,val,sizeof(in)) 
#define mp make_pair 
#define sol first
#define Y second
#define pb push_back
#define rep(i,in,b) for(int i=in;i<b;i++)
/*Use like- 
rep(i,0,n - 1)
*/
template<class T> T pwr(T b, T p){T r=1,sol=b;while(p){if(p&1)r*=sol;sol*=sol;p=(p>>1);}return r;}
 
#define     inf             (0x7f7f7f7f) 

vector<int> Fix(int len)
{
    vector<int> ans;
    ans.push_back(1);
    for(int i=0; i<len-2;i++)
        ans.push_back(rand()%2);
    ans.push_back(1);
    return ans;
}

inline vector<int> PreCompute( int n )
{
    vector<char> ans(n+1, true);
    ans[1] = false;
    for ( int i = 2; i*i <= n; i++ )
        if ( ans[i] )
            for ( int j = i * i; j <= n; j+= i )
                ans[j] = false;
    vector<int> res;
    for ( int i = 2; i <= n; i++ )
        if ( ans[i] ) res.push_back(i);
    return res;
}

vector<int> Primes;

int check(ll num)
{
    for ( int v : Primes ){
        if ( v >= num ) break;
        if ( num % v == 0){
            return v;
        }
    }
    
    return 0;
}

ll solve(vector<int> &v, int base)
{
    ll res = 0;
    ll p = 1;
    
    for ( int i = v.size() - 1; i >= 0; i-- ){
        res += p * v[i];
        p *= base;
    }
    
    return res;
}

int main()
{
    //freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);       
    Primes = PreCompute(1e5);    
    set<pair<vector<int>, vector<int> > > ans;
    while ( ans.size() < 50 )
    {
        auto apair = Fix(16);
        
        vector<int> v;
        for(int i=2; i<=10;i++)

        {
            ll number = solve(apair, i);
            if ( int k = check(number) )
                v.push_back(k);
        }
        
        if ( v.size() == 9 ){
            ans.insert(mp(apair, v));
        }
    }
    
    printf ( "Case #1:\n" );
    
    for ( auto &apair : ans )
    {
        for(int i=0; i<apair.first.size();i++) 
        cout<<apair.first[i];
        for(int i=0; i<9;i++)
        cout<<" "<<apair.second[i];
        
        puts("");
    }
    
    return 0;
}