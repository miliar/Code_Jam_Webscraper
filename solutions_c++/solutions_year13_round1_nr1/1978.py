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

int main()
{
    int T;
    cin>>T;
    REP(tt, T)
    {
      unsigned long long int r,t;
      cin>>r>>t;
      unsigned long long int paintUsed = 0;
      unsigned long long int circlesPainted = 0;
      unsigned long long int d = 2*r;
      for(unsigned long long int i=0;;i+=2)
      {
          paintUsed += ((i+1) + i) + d;
          //cout<<paintUsed<<" ";
          if(paintUsed > t) {break;}
          else {circlesPainted++;}   
      }
      cout<<"Case #"<<(tt+1)<<": "<<circlesPainted<<endl;
    }
    //int t;cin>>t;
    return 0; 
}
