// There is nothing in a caterpillar that tells you its going to be a butterfly!
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <bitset>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
using namespace std;

#define ll long long
#define pi pair<ll,ll>
#define f first
#define s second
#define pb push_back
#define rep(i,n) for(int i=0;i<n;i++)
#define mod 1000000007
int test;
bool vis[2011][10];

int main(){
    //freopen("A-small-attempt0.in.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int T;
    cin >> T;
    rep(i,T){
        string s;
        cin >> s;
        int f[26]={0};
        for(auto x:s){
            f[x-'A']++;
        }
        int dig[10]={0};
        string ans="";
        while(f[25]) ans+='0' , dig[0]++ , f['Z'-'A']-- , f['E'-'A']-- , f['R'-'A']-- , f['O'-'A']--;
        while(f['U'-'A']) ans+='4' , dig[4]++ , f['F'-'A']-- , f['O'-'A']-- , f['U'-'A']-- , f['R'-'A']--;
        while(f['W'-'A']) ans+='2' , dig[2]++ , f['T'-'A']-- , f['W'-'A']-- , f['O'-'A']--;
        while(f['X'-'A']) ans+='6' , dig[6]++ , f['S'-'A']-- , f['I'-'A']-- , f['X'-'A']--;
        while(f['G'-'A']) ans+='8' , dig[8]++ , f['E'-'A']-- , f['I'-'A']-- , f['G'-'A']-- , f['H'-'A']-- , f['T'-'A']--;
        while(f['O'-'A']) ans+='1' , f['O'-'A']-- , f['N'-'A']-- , f['E'-'A']--;
        while(f['T'-'A']) ans+='3' , f['T'-'A']-- , f['H'-'A']-- , f['R'-'A']-- , f['E'-'A']-=2;
        while(f['F'-'A']) ans+='5' , f['F'-'A']-- , f['I'-'A']-- , f['V'-'A']-- , f['E'-'A']--;
        while(f['I'-'A']) ans+='9' , f['N'-'A']-- , f['I'-'A']-- , f['N'-'A']-- , f['E'-'A']--;
        while(f['S'-'A']) ans+='7', f['S'-'A']-- , f['E'-'A']-- , f['V'-'A']-- , f['E'-'A']-- , f['N'-'A']--;
        
        sort(ans.begin(),ans.end());
        cout<<"Case #"<<i+1<<": "<<ans<<"\n";
    }
}