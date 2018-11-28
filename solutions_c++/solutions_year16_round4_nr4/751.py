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

template <typename T>
class Point2
{
public:
  Point2(){}
  Point2(T x_, T y_):x(x_), y(y_) {}

  bool       operator ==(const Point2<T>&) const;
  bool       operator !=(const Point2<T>&) const;

  Point2<T>& operator +=(const Point2<T>&);
  Point2<T>& operator -=(const Point2<T>&);
  Point2<T>& operator /=(T);
  Point2<T>& operator *=(T);

  T length() const;
  T length_square() const;

public:
  T x;
  T y;
};


typedef Point2<int>       Point2I;

bool choose(int ws[4][4], vector<int>& used_w, vector<int>& used_m, int left, int n)
{
  if (!left)
    return true;

  FOR (w,0,n)
  {
    if (!used_w[w])
    {
      used_w[w]=1;
      bool ok=true;
      bool m_exists=false;
      FOR (m,0,n)
      {
        if (!used_m[m]&&ws[w][m])
        {
          m_exists=true;
          used_m[m]=1;
          bool res=choose(ws,used_w,used_m,left-1,n);
          used_m[m]=0;
      
          if (!res)
          {
            ok=false;
            break;
          }
        }
      }
      used_w[w]=0;

      if(!ok||!m_exists)
        return false;
    }
  }

  return true;
}

bool avail(int n, int w[4][4])
{
  return choose(w,vector<int>(n,0),vector<int>(n,0),n,n);
  //vector<int> order(n);
  //FOR (i,0,n)
  //  order[i]=i;

  //bool ok=true;
  //do 
  //{
  //  vector<int> used(n,0);

  //  FOR (j,0,n)

  //} while (ok && next_permutation(order.front(),order.front()+n));
  //return ok;
}

void main()
{
  ifstream is("GoogleCodeJam/D-small-attempt0.in");
  //ifstream is("GoogleCodeJam/input.txt");
  ofstream os("GoogleCodeJam/output.txt");

  int t;
  is>>t;

  int w[4][4];

  for (int ti=0;ti<t;++ti)
  {
    //solve
    int n;
    is>>n;

    vector<Point2I> ps;

    FOR (i,0,n)
    {
      string s;
      is>>s;
      FOR (j,0,n)
      {
        w[i][j]=s[j]-'0';
        if (!w[i][j])
          ps.push_back(Point2I(i,j));
      }
    }

    int res=1000000;
    FOR (mask,0,1<<ps.size())
    {
      FOR (j,0,ps.size())
      {
        if (get_bit(mask,j))
          w[ps[j].x][ps[j].y]=1;
      }
      if (avail(n,w))
      {
        int k=0;
        FOR (j,0,16)
          k+=get_bit(mask,j);
        res=min(k,res);
      }
      FOR (j,0,ps.size())
      {
        if (get_bit(mask,j))
          w[ps[j].x][ps[j].y]=0;
      }
    }

    os << "Case #"<<ti+1<<": "<<res;
    //out
    os<<"\n";
  }
}




//
//template <typename T>
//class Point3
//{
//public:
//  Point3(){}
//  Point3(T x_, T y_, T z_):x(x_), y(y_), z(z_) {}
//
//  bool       operator ==(const Point3<T>&) const;
//  bool       operator !=(const Point3<T>&) const;
//
//  Point3<T>& operator +=(const Point3<T>&);
//  Point3<T>& operator -=(const Point3<T>&);
//  Point3<T>& operator /=(T);
//  Point3<T>& operator *=(T);
//
//  T length() const;
//  T length_square() const;
//
//public:
//  T x;
//  T y;
//  T z;
//};
//
//template<class T>
//inline Point3<T>& Point3<T>::operator +=(const Point3<T>& r)           
//{
//  x += r.x;
//  y += r.y;
//  z += r.z;
//  return *this;
//}
//typedef Point3<int>    Point3I;
//
//struct S
//{
//  S():p(0,0,0){}
//  S(int i):p(0,0,0){i==0?p.x=1:(i==1?p.y=1:p.z=1);}
//  Point3I p;
//};
//
//typedef pair<string,S> R;
//
//template<class T>
//inline bool Point3<T>::operator == (const Point3<T>& p) const          
//{
//  return x == p.x && y == p.y && z == p.z;
//}
//
//void main()
//{
//  //ifstream is("GoogleCodeJam/A-small-attempt0.in");
//  ifstream is("GoogleCodeJam/A-large.in");
//  //ifstream is("GoogleCodeJam/input.txt");
//  ofstream os("GoogleCodeJam/output.txt");
//
//  pair<string,S> dp[12+1][3];
//  char ic[3]={'P','R','S'};
//  FOR (i,0,3)
//  {
//    dp[0][i]=make_pair(string(1,ic[i]),S(i));
//  }
//  FOR (h,1,12+1)
//    FOR (i,0,3)
//  {
//    R& r0=dp[h-1][i];
//    R& r1=dp[h-1][(i+1)%3];
//    dp[h][i].first=min(r0.first,r1.first)+max(r0.first,r1.first);
//    dp[h][i].second.p+=r0.second.p;
//    dp[h][i].second.p+=r1.second.p;
//  }
//
//  int t;
//  is>>t;
//
//  for (int ti=0;ti<t;++ti)
//  {
//    //solve
//    int n, r, p, s;
//    is>>n>> r>> p>> s;
//
//    //p->,r->,s
//    os << "Case #"<<ti+1<<": ";
//    //out
//    string res;
//    Point3I prs(p,r,s);
//    FOR (i,0,3)
//    {
//      R& r=dp[n][i];
//      if (r.second.p==prs&&(res.empty()||r.first<res))
//      {
//        res=r.first;
//      }
//    }
//
//    if (!res.empty())
//      os<<res;
//    else
//      os<<"IMPOSSIBLE";
//
//    os<<"\n";
//  }
//}




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


