/* Created by Anmol Varshney */

#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define ARRAY_SIZE(arr) sizeof(arr)/sizeof(arr[0])
#define INT_MIN -2147483647
#define INT_MAX 2147483647
#define INF_LL 9223372036854775807LL
#define PI acos(-1.0)
#define llu long long unsigned
#define ll long long int
#define ld long int
#define iter(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define REP(p,a,b) for(int p=a;p<b;p++)
#define mod 1000000007
#define getchar_unlocked getchar
#define pb(f) push_back(f)
#define pob(f) pop_back(f)
#define pf(f) push_front(f)
#define pof(f) pop_front(f)
#define mkp(a,b) make_pair(a,b)
#define fst first
#define snd second
#define pii pair<int,int>
#define ins(a) insert(a)
#define IOS ios_base::sync_with_stdio(false)
#define citi cin.tie(NULL);
#define FREI(var) freopen(var,"r",stdin)
#define FREO(var) freopen(var,"w",stdout)


int gcd(int a,int b)
{
    if(b>a) return gcd(b,a);
    else if(b!=0) return gcd(b,a%b);
    else return a;
}

string to_string(int num)
{
    stringstream ss;
    ss << num;
    return ss.str();
}

int cnt[26];
string s;
vector<int> v;


int main() {
    FREI("input.in");
    FREO("output.txt");
    IOS;
    citi;
    int te,ind;
    cin>>te;
    REP(l,1,te+1)
    {
        v.clear();
        memset(cnt,0,sizeof(cnt));
        cin>>s;
        REP(i,0,s.size())
            cnt[s[i]-'A']++;
        cout<<"Case #"<<l<<": ";
        REP(i,0,cnt['Z'-'A'])
            v.pb(0);
        cnt['E'-'A']-=cnt['Z'-'A'];
        cnt['R'-'A']-=cnt['Z'-'A'];
        cnt['O'-'A']-=cnt['Z'-'A'];
        cnt['Z'-'A']=0;
        REP(i,0,cnt['W'-'A'])
            v.pb(2);
        cnt['T'-'A']-=cnt['W'-'A'];
        cnt['O'-'A']-=cnt['W'-'A'];
        cnt['W'-'A']=0;
        REP(i,0,cnt['U'-'A'])
            v.pb(4);
        cnt['F'-'A']-=cnt['U'-'A'];
        cnt['O'-'A']-=cnt['U'-'A'];
        cnt['R'-'A']-=cnt['U'-'A'];
        cnt['U'-'A']=0;
        REP(i,0,cnt['X'-'A'])
            v.pb(6);
        cnt['S'-'A']-=cnt['X'-'A'];
        cnt['I'-'A']-=cnt['X'-'A'];
        cnt['X'-'A']=0;
        REP(i,0,cnt['O'-'A'])
            v.pb(1);
        cnt['N'-'A']-=cnt['O'-'A'];
        cnt['E'-'A']-=cnt['O'-'A'];
        cnt['O'-'A']=0;
        REP(i,0,cnt['R'-'A'])
            v.pb(3);
        cnt['T'-'A']-=cnt['R'-'A'];
        cnt['H'-'A']-=cnt['R'-'A'];
        cnt['E'-'A']-=2*cnt['R'-'A'];
        cnt['R'-'A']=0;
        REP(i,0,cnt['S'-'A'])
            v.pb(7);
        cnt['E'-'A']-=2*cnt['S'-'A'];
        cnt['V'-'A']-=cnt['S'-'A'];
        cnt['N'-'A']-=2*cnt['S'-'A'];
        cnt['S'-'A']=0;
        REP(i,0,cnt['V'-'A'])
            v.pb(5);
        cnt['F'-'A']-=cnt['V'-'A'];
        cnt['I'-'A']-=cnt['V'-'A'];
        cnt['E'-'A']-=cnt['V'-'A'];
        cnt['V'-'A']=0;
        REP(i,0,cnt['G'-'A'])
            v.pb(8);
        cnt['E'-'A']-=cnt['G'-'A'];
        cnt['I'-'A']-=cnt['G'-'A'];
        cnt['H'-'A']-=cnt['G'-'A'];
        cnt['T'-'A']=-cnt['G'-'A'];
        cnt['G'-'A']=0;
        REP(i,0,cnt['E'-'A'])
            v.pb(9);
        sort(v.begin(),v.end());
        REP(k,0,v.size())cout<<v[k];
        cout<<endl;
    }
    return 0;
}
