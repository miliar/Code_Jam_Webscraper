#define _USE_MATH_DEFINES //for math constants definitions in math.h
#include <assert.h>
#include <math.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
typedef long long     ll;
typedef unsigned int  UInt;
#define FOR(i,a,b)      for(int i = a;   i <  (int)(b); ++i)
#define FOR_REV(i,a,b)  for(int i = b-1; i >= (int)(a); --i)
template<class T> inline T   sqr(T v)  { return v * v; }
template<class T> inline int sign(T v) { return v == 0 ? 0 : (v > 0 ? 1 : -1); }
template<class T> int get_bit(T v, int bit_index) { return (v >> bit_index) & 1; } //return {0,1}

//////////////////////////////////////////////////////////////////////////


//////////////////////////////////////////////////////////////////////////
//Point3<T>
//////////////////////////////////////////////////////////////////////////

template <typename T>
class Point3
{
public:
  Point3(){}
  Point3(T x_, T y_, T z_):x(x_), y(y_), z(z_) {}

  bool       operator ==(const Point3<T>&) const;
  bool       operator !=(const Point3<T>&) const;

  Point3<T>& operator +=(const Point3<T>&);
  Point3<T>& operator -=(const Point3<T>&);
  Point3<T>& operator /=(T);
  Point3<T>& operator *=(T);

  T length() const;
  T length_square() const;

public:
  T x;
  T y;
  T z;
};

template<class T>
inline Point3<T>& Point3<T>::operator +=(const Point3<T>& r)           
{
  x += r.x;
  y += r.y;
  z += r.z;
  return *this;
}
typedef Point3<int>    Point3I;

struct S
{
  S():p(0,0,0){}
  S(int i):p(0,0,0){i==0?p.x=1:(i==1?p.y=1:p.z=1);}
  Point3I p;
};

typedef pair<string,S> R;

template<class T>
inline bool Point3<T>::operator == (const Point3<T>& p) const          
{
  return x == p.x && y == p.y && z == p.z;
}

//vector<int> try_(vector<int> a, int prs[3], int h)
//{
//  int prs_need[3]={0,0,0};
//  FOR (i,0,a.size())
//    prs_need[a[i]]++;
//  if (prs_need[0]>prs[0]||prs_need[1]>prs[1]||prs_need[2]>prs[2])
//    return vector<int>();
//  if (h==0)
//    return a;
//
//  //w=0..2
//  vector<int> b(a.size()*2);
//  FOR (i,0,a.size())
//  {
//    b[i*2]=a[i];
//    b[i*2+1]=(a[i]+1)%3;
//  }
//  return try_(b, prs, --h);
//}
//
//string try_(int w, int prs[3], int h)
//{
//  vector<int> res =try_(vector<int>(1,w),prs,h);
//  if (!res.empty())
//  {
//    string resc(res.size(),0);
//    FOR (i,0,res.size())
//    {
//      resc[i]=ic[res[i]];;
//    }
//    return resc;
//  }
//  else
//    return "";
//}

void main()
{
  //ifstream is("GoogleCodeJam/A-small-attempt0.in");
  ifstream is("GoogleCodeJam/A-large.in");
  //ifstream is("GoogleCodeJam/input.txt");
  ofstream os("GoogleCodeJam/output.txt");

  pair<string,S> dp[12+1][3];
  char ic[3]={'P','R','S'};
  FOR (i,0,3)
  {
    dp[0][i]=make_pair(string(1,ic[i]),S(i));
  }
  FOR (h,1,12+1)
    FOR (i,0,3)
  {
    R& r0=dp[h-1][i];
    R& r1=dp[h-1][(i+1)%3];
    dp[h][i].first=min(r0.first,r1.first)+max(r0.first,r1.first);
    dp[h][i].second.p+=r0.second.p;
    dp[h][i].second.p+=r1.second.p;
  }

  int t;
  is>>t;

  for (int ti=0;ti<t;++ti)
  {
    //solve
    int n, r, p, s;
    is>>n>> r>> p>> s;

    //p->,r->,s
    os << "Case #"<<ti+1<<": ";
    //out
    string res;
    Point3I prs(p,r,s);
    FOR (i,0,3)
    {
      R& r=dp[n][i];
      if (r.second.p==prs&&(res.empty()||r.first<res))
      {
        res=r.first;
      }
    }

    if (!res.empty())
      os<<res;
    else
      os<<"IMPOSSIBLE";

    os<<"\n";
  }
}




//void main()
//{
//  //ifstream is("GoogleCodeJam/A-small-attempt0.in");
//  //ifstream is("GoogleCodeJam/A-large.in");
//  ifstream is("GoogleCodeJam/input.txt");
//  ofstream os("GoogleCodeJam/output.txt");
//
//  int t;
//  is>>t;
//
//  for (int ti=0;ti<t;++ti)
//  {
//    //solve
//
//    os << "Case #"<<ti+1<<": ";
//    //out
//    os<<"\n";
//  }
//}


