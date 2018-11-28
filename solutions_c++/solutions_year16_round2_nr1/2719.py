#include <bits/stdc++.h>

typedef long long LL;
typedef unsigned long long ULL;
typedef long double ld;
typedef __float128 bfl;

const int MOD = 1000000007;

#define f first
#define s second
#define pll pair<LL, LL> 
#define pii pair<int, int> 
#define mp make_pair
#define pb push_back
#define SC static_cast

using namespace std;
string s;
int m[40];
int zero[40], one[40], two[40], three[40], five[40],four[40],
    six[40], seven[40], eight[40], nine[40];

vector<int> ans;

void solve(int k)
{
    ans.clear();
    for(int i = 0; i<40; i++) m[i] = 0;

    cin>>s;
    for(int i = 0; i<s.size(); i++)
        m[s[i]-'A']++;
    
    int cnt = m['Z'-'A'];
    for(int i = 0; i<40; i++) 
        m[i]-=zero[i]*cnt;
    for(int i = 0; i<cnt; i++) 
        ans.pb(0);

    cnt = m['X'-'A'];
    for(int i = 0; i<40; i++) 
           m[i]-=six[i]*cnt;
    
    for(int i = 0; i<cnt; i++) 
        ans.pb(6);
    
    cnt = m['W'-'A'];
    for(int i = 0; i<40; i++) 
           m[i]-=two[i]*cnt;
    for(int i = 0; i<cnt; i++) 
        ans.pb(2);
    
    cnt = m['S'-'A'];
    for(int i = 0; i<40; i++) 
           m[i]-=seven[i]*cnt;
    
    for(int i = 0; i<cnt; i++) 
        ans.pb(7);
    
    cnt = m['V'-'A'];
    for(int i = 0; i<40; i++) 
           m[i]-=five[i]*cnt;
    
    for(int i = 0; i<cnt; i++) 
        ans.pb(5);
    
    cnt = m['U'-'A'];
    for(int i = 0; i<40; i++) 
           m[i]-=four[i]*cnt;
    for(int i = 0; i<cnt; i++) 
        ans.pb(4);
    
    
    cnt = m['O'-'A'];
    for(int i = 0; i<40; i++) 
         m[i]-=one[i]*cnt;
    for(int i = 0; i<cnt; i++) 
        ans.pb(1);
    
    
    cnt = m['G'-'A'];
    for(int i = 0; i<40; i++) 
           m[i]-=eight[i]*cnt;
    for(int i = 0; i<cnt; i++) 
        ans.pb(8);
    
    
    cnt = m['N'-'A']/2;
    for(int i = 0; i<40; i++) 
           m[i]-=nine[i]*cnt;
    for(int i = 0; i<cnt; i++) 
        ans.pb(9);
    
    
    cnt = m['T'-'A'];
    for(int i = 0; i<40; i++) 
           m[i]-=three[i]*cnt;
    for(int i = 0; i<cnt; i++) 
        ans.pb(3);
    
    
    sort(ans.begin(), ans.end());
    cout<<"Case #"<<k<<": ";
    for(int i =0; i<ans.size(); i++)
        cout<<ans[i];
    cout<<endl;
}

int main()
{
    zero['Z'-'A']++;
    zero['E'-'A']++;
    zero['R'-'A']++;
    zero['O'-'A']++;

    one['O'-'A']++;
    one['N'-'A']++;
    one['E'-'A']++;
    
    two['T'-'A']++;
    two['W'-'A']++;
    two['O'-'A']++;
    
    three['T'-'A']++;
    three['H'-'A']++;
    three['R'-'A']++;
    three['E'-'A']++;
    three['E'-'A']++;

    four['F'-'A']++;
    four['O'-'A']++;
    four['U'-'A']++;
    four['R'-'A']++;
    
    five['F'-'A']++;
    five['I'-'A']++;
    five['V'-'A']++;
    five['E'-'A']++;
    
    six['S'-'A']++;
    six['I'-'A']++;
    six['X'-'A']++;
    
    seven['S'-'A']++;
    seven['E'-'A']++;
    seven['V'-'A']++;
    seven['E'-'A']++;
    seven['N'-'A']++;
    
    eight['E'-'A']++;
    eight['I'-'A']++;
    eight['G'-'A']++;
    eight['H'-'A']++;
    eight['T'-'A']++;
    
    nine['N'-'A']++;
    nine['I'-'A']++;
    nine['N'-'A']++;
    nine['E'-'A']++;
    
    int t;
    cin>>t;
    for(int i = 0; i<t; i++)
        solve(i+1);
    return 0;
}
