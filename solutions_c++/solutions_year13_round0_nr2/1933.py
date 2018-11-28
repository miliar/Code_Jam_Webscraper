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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits.h>
#include <string.h>
 
#define repx(i,x,n) for(int i=x;i<n;i++)
#define rep(i,n) repx(i,0,n)
#define pb push_back
#define full(v)  v.begin(),v.end()
#define np next_permutation
#define VI vector<int>
#define VS vector<string>
#define VC vector<char>
#define VD vector<double>
#define VF vector<float>
#define SI set<int>
#define SC set<char>
#define SS set<string>
#define MII map<int,int>
#define MSI map<string,int>
#define MIS map<int,string>
#define MIC map<int,char>
#define MCI map<char,int>
#define LL long long
using namespace std;

int main()
{
    ofstream cout ("Bbig.out");
    ifstream cin ("Bbig.in");
 
    int test,cas=0;
    cin>>test;
    while(test-- && ++cas)
    {
     vector <vector <int> > v;
     int rows[103],cols[103];
     memset(rows,-1,sizeof(rows));
     memset(cols,-1,sizeof(cols));
     int n,m;
     cin>>n>>m;
     rep(i,n)
     {
             vector <int> temp;
             rep(j,m)
             {
                     
                     int t;
                     cin>>t;
                     rows[i] = max(rows[i],t);
                     temp.pb(t);
             }
             v.pb(temp);
     }
     rep(j,m)
     {
      rep(i,n)
      {
              cols[j] = max(v[i][j] , cols[j]);
      }       
     }
     
     bool flag = true;
     rep(i,n)
     rep(j,m)
     if(! (rows[i] == v[i][j] || cols[j] == v[i][j]))
     {
          flag = false;
          i=j=(m+n+1);
     }
      cout<<"Case #"<<cas<<": ";
    
     if(flag)
             cout<<"YES\n";
     
     else
         cout<<"NO\n";
     
    }
    return 0;
}
