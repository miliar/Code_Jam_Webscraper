
#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;

#define X           first
#define Y           second
#define F0(i,n)     for(int i=0;i<(n);i++)
#define FOR(i,a,b)  for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FORE(i,x)   for( auto i=(x).begin();i != (x).end();++i)
#define ALL(x)      (x).begin(),(x).end()
#define CLR(x,w)    memset((x),w,sizeof (x))
#define PU          push_back
#define MP          make_pair


int main()
{
 int _T;
 long long n,s,e,w,v1,v2,v3,v4,f=0,c=0;
 cin>>_T;
 string str="";
 v1=0;
 v2=0;
 FOR(_t,1,_T)
 {
   v1=0;
   v2=0;
   f=0;
   c=0;
   str="";
   cin>>v3>>v4;
   
   while(1)
   {
    c++;
    if(f==2)
     break;
     
     if(v3<v4)
     {
       if(v1+c==v3)
       {
        str=str+"E";
        v3=v4+1;
        v1=v1+c;
        f++;
       }
       else if(v1+c<v3)
       {
        str=str+"E";
        v1=v1+c;
       }
       else
       {
        str=str+"W";
         v1=v1-c;
        }
      }
      else
      {
       if(v2+c==v4)
       {
        str=str+"N";
        v2=v2+c;
        v4=v3+1;
        f++;
       }
       else if(v2+c<v4)
       {
        str=str+"N";
        v2=v2+c;
       }
       else
       {
        str=str+"S";
         v2=v2-c;
        }
      }
      cerr<<str<<" "<<v1<<"  "<<v2<<endl;
     } 
   cout<<"Case #"<<_t<<": "<<str<<endl;
 }

 return 0;
}
