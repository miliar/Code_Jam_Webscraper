
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

#define PI 3.14159265358979323846264338327950288
int main()
{
 int _T;
  
 cin>>_T;
 FOR(_t,1,_T)
 {
   long double r,t,c=-1;
   cin>>r>>t;
   cerr<<" input "<<r <<" "<<t<<endl;
   long double rp=0;
   while( (t-rp)>=0)
   {
     rp = rp + ((r+1)*(r+1))-(r*r);
     cerr<<"rp = "<< rp<<endl;
     r= r+2;
     c++;
   }
   cout<<"Case #"<<_t<<": "<<c<<endl;
 }

 return 0;
}
