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
 
#define repx(i,x,n) for(long long i=x;i<n;i++)
#define rep(i,n) repx(i,0,n)
#define pb push_back
#define full(v)  v.begin(),v.end()
#define np next_permutation
#define VI vector<long long>
#define VS vector<string>
#define VC vector<char>
#define VD vector<double>
#define VF vector<float>
#define SI set<long long>
#define SC set<char>
#define SS set<string>
#define MII map<long long,long long>
#define MSI map<string,long long>
#define MIS map<long long,string>
#define MIC map<long long,char>
#define MCI map<char,long long>
#define LL long long
using namespace std;
bool isPalindrome(long long n)
{
     long long t = n;
     long long ret=0;
     while(t)
     {
      ret = (ret*10) + (t%10);
      t = t/10;
     }
     if(ret == n)
      return true;
     return false;
}

int main()
{
    ofstream cout ("Cbig.out");
    ifstream cin ("Cbig.in");
   vector <LL> res;
   rep(i,10000001)
     {
      
             if(isPalindrome(i) && isPalindrome(i*i))
                   res.pb(i*i);
       
     }
    long long test,cas=0;
    cin>>test;
    while(test-- && ++cas)
    {
     long long a,b;
     cin>>a>>b;
     long long ret = 0;
     rep(i,res.size())
     {
      if(res[i] >= a && res[i] <=b)
       {
             ret++;
       }
     }
     cout<<"Case #"<<cas<<": "<<ret<<"\n";
    
    }
    return 0;
}
