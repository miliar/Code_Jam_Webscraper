#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)
typedef unsigned long long int ull;

bool isConst(char a)
{
   return (!((a=='i') || (a == 'a') || (a=='e') || (a=='o') || (a=='u')));
}

int main()
{
    int T;
    cin>>T;
    REP(tt, T)
    {
      string s;
      int n;
      cin>>s>>n;
      int len = s.length();
      ull count = 0;
      ull cc = 0;
      bool first = true;
      for(int i=0; i<len; i++)
      {
         first = true;
         cc=0;
         for(int j=i+n-1; j<len;j++)
         {
              if(first)
              {
                 for(int k=j;k>=i;k--){
                   if(isConst(s[k]))
                     cc++;
                   else
                     break;
                 }
                 first = false;
                 if(cc == n) {count += (len-j); break;}
              }else{
                 if(isConst(s[j])){cc++;}
                 else cc = 0;
                 if(cc == n) {count += (len-j); break;}    
              }
         }
      }
      cout<<"Case #"<<(tt+1)<<": "<<count<<endl;      
    }
    //int t;cin>>t;
    return 0; 
}
