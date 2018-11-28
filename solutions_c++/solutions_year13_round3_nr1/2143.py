#include <iostream>
#include <fstream>

#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <numeric>


#include <algorithm>
#include <functional>
#include <sstream>
#include <utility>

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include "gmpxx.h"
typedef mpz_class big;

using namespace std;

typedef vector<int>     vi;
typedef pair<int,int>   ii;
typedef vector<ii>      vii;
typedef long long       ll;
typedef set<int>        si;
typedef map<string,int> msi;

#define sz(a)   int((a).size())
#define all(c)  (c).begin(),(c).end()
#define pb(a)      push_back(a);
#define rep(i,n)    for(int i(0);i<int(n);i++)
#define TRvi(c,it)  for(vi::iterator it=(c).begin();it!=(c).end();it++)
#define INF 2E9

bool iscons(char a)
{
    return (!(a=='a' || a=='e' || a=='i' || a=='o' || a=='u'));
}
int main()
{
    ifstream cin("A-small-attempt0(3).in");
    ofstream cout("out.txt");
    int T;
    cin>>T;
    rep(i,T){   // For each test case
        cout<<"Case #"<<i+1<<": ";      // Print Case #i:
        string t; int ncons;
        cin>>t>>ncons;
        int cnt(0);
        int last(0);
        int ans(0);
        rep(i,t.size()){
            if(iscons(t[i])){
                cnt++;
                if(cnt>=ncons){
                    int lchar(i-ncons+1);
                    int left=lchar-last;
                    int right=t.size()-1-i;
                    if(left==0){left=1; right+=1;}
                    else if(right==0){right=1; left+=1;}
                    else {left+=1; right+=1;};
                    ans+=left*right;
                    last=lchar+1;
                }
            }
            else cnt=0;
        }

        cout<<ans<<endl;
    }
    return 0;
}
