#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <cassert>
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
#include <cstring>
#include<stdio.h>

#define uniq(c) (c).resize(unique(c.begin(),c.end())-(c).begin());
#define all(a) a.begin(),a.end()
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define pb push_back
#define PI 3.14159265
#define eps 1e-10
#define LL long long
#define ULL unsigned long long
#define MOD 1000000007



using namespace std;
int SI(string st) {int ans; stringstream s; s<<st; s>>ans; return ans;}
string IS(int n) {string str; stringstream s; s<<n; s>>str; return str;}

int main()
{
    freopen("read.txt","r",stdin);
    freopen("write.txt","w",stdout);
    int t,sm,tt = 1;
    string s;
    cin>>t;
    while(t--)
    {
        long int ans = 0,ps = 0;
        cin>>sm;cin>>s;
        FOR(i,0,s.length())
        {
            if(s[i] > '0')
            {
                if (ps >=i)
                 {
                   ps += (s[i] -'0');
                 }
               else
                 {
                   ans += (i-ps);
                   ps += (s[i] - '0') + (i-ps);
                 }
             }   
             //cout<<ans<<" "<<ps<<"\n"; 
        }
        cout<<"Case #"<<tt++<<": "<<ans<<"\n";
    }
    
}
