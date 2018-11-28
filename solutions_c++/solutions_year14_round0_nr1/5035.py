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
int SI(string str) {int ans; stringstream s; s<<str; s>>ans; return ans;}
string IS(int n) {string str; stringstream s; s<<n; s>>str; return str;}

int main()
{
    freopen("read.txt","r",stdin);
    freopen("write.txt","w",stdout);
    int t;
    int a[4][4],b[4][4],ans1,ans2;
    cin>>t;
    FOR(tt,1,t+1)
    {
        cin>>ans1;
        FOR(i,0,4)   FOR(j,0,4) cin>>a[i][j];
        cin>>ans2;
        FOR(i,0,4)   FOR(j,0,4) cin>>b[i][j];
        int h1[4],h2[4];
        FOR(i,0,4) h1[i] = a[ans1-1][i];
        FOR(i,0,4) h2[i] = b[ans2-1][i];
        int c = 0,ans;
        FOR(i,0,4)
        {
            FOR(j,0,4)
            {
                if(h1[i] == h2[j])
                {
                    c++;
                    ans = h1[i];
                }
            }
        }
        if(c==1) cout<<"Case #"<<tt<<": "<<ans<<"\n";
        if(c>1) cout<<"Case #"<<tt<<": Bad magician!"<<"\n";
        if(c==0) cout<<"Case #"<<tt<<": Volunteer cheated!"<<"\n";
    }   
    return 0;
}
