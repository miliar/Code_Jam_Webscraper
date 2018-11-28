#include <iostream>
#include <string.h>
#include <string>
#include <math.h>
#include <stdio.h>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <list>
#include <vector>
#include <deque>
#include <functional>

typedef long long ll;
typedef unsigned long long ull;

#define pb push_back()
#define pf push_front()
#define popb pop_back()
#define popf pop_front()
//#define rall(v) v.begin(),v.end(),greater<double>()
//#define all(v) v.begin(),v.end()
//#define SZ(x) size(x)
#define pii 2*acos(0)
#define max 1000
//#define FOR(i,n) for (int i=0;i<int n ;i++)
//#define FOR1(i,n) for (int i=1;i<=int n ;i++)
//#define RF0(i,n) for (int i=(int n)-1 ;i>=0 ;i--)


using namespace std;


int main()
{
    double ptr,t,a,b,c,d,e,i,j,k,p,count,p1,p2,child;
    vector<double> v;
    char ch;
    int q,l,ans;
    list<double> ilist;
    deque<double> v1;

string si;
    //char ch[max];
    //string str[max];
    int simax,final_total;
freopen("A-large.in","r",stdin);
    freopen("o.out","w",stdout);

    cin>>t;
     for (i=0;i<t;i++)
     {final_total=0;
     count=0;
      cin>>simax>>si;
      for (j=0;j<=simax;j++)
      {
          if (final_total<j)
          {
              count+=j-final_total;
              final_total+=si[j]-48+j-final_total;
          }
          else
          final_total+=si[j]-48;
      }
      cout<<"Case #"<<i+1<<": "<<count<<endl;
     }
    return 0;
}
