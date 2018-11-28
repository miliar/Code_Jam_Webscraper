#include <assert.h>
#include <vector>
#include <list>
#include <map>
#include <math.h>
#include <set>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
typedef long long ll;
#define FOR(i,a,b)    for(int i=a;i<(int)b;++i)
#define FOR_D(i,a,b)  for(int i=a;i>=b;--i)
template<class T> inline T   sqr(T v)  { return v * v; }
template<class T> inline int sign(T v) { return v == 0 ? 0 : (v > 0 ? 1 : -1); }

//a - ���� ���������������� �� �����-�� �����. ����������� ���-��, ��� ������ � 0 ����������, � ��������� ������ ����� ���-�. it_max=70 ��� n<=10^6
//b - �� ���� ����� � big �����
//c - ����� ����������� �� ������ ������� ���������: ���� �� �������� � ������������
//d - ���� ������ small

//////////////////////////////////////////////////////////////////////////

//a
void main()
{
  ifstream is("GoogleCodeJam/A-large.in");
  //ifstream is("GoogleCodeJam/input.txt");
  ofstream os("GoogleCodeJam/output.txt");

  int t;
  is>>t;

  for (int ti=0;ti<t;++ti)
  {
    ll n;
    is>>n;

    int it_max=0;
    //for (n=1;n<=1000000;++n)
    {
      vector<int> use(10,0);
      int use_k=0;
      ll nn=n;

      for (int it=0;it<100000;++it,nn+=n)
      {
        for (ll k=nn;;)
        {
          if (!use[k%10])
          {
            use[k%10]=1;
            ++use_k;
          }
          k/=10;
          if (!k)
            break;
        }
        if (use_k==10)
          break;
        it_max=max(it_max,it);
      }

      os << "Case #"<<ti+1<<": ";
      //os << "Case #"<<n<<": ";
      use_k==10? os<<nn : os<<"INSOMNIA";
      os<<"\n";
    }

    //cout<<"it_max = "<<it_max<<endl;
  }
}

////d-small
//void main()
//{
//  ifstream is("GoogleCodeJam/D-small-attempt0.in");
//  //ifstream is("GoogleCodeJam/input.txt");
//  ofstream os("GoogleCodeJam/output.txt");
//
//  int t;
//  is>>t;
//
//  for (int ti=0;ti<t;++ti)
//  {
//    int k,c,s;
//    is>>k>>c>>s;
//
//    os << "Case #"<<ti+1<<": ";
//    FOR (i,1,k+1)
//      os<<i<<" ";
//    os<<"\n";
//  }
//}

////b
//void main()
//{
//  ifstream is("GoogleCodeJam/B-small-attempt0.in");
//  ofstream os("GoogleCodeJam/output.txt");
//
//  int t;
//  is>>t;
//
//  for (int ti=0;ti<t;++ti)
//  {
//    string s;
//    is>>s;
//    int res=0;
//    FOR (i,1,s.size())
//      if (s[i]!=s[i-1])
//        ++res;
//    if (s.back()=='-')
//      ++res;
//
//    os << "Case #"<<ti+1<<": ";
//    os<<res;
//    os<<"\n";
//  }
//}

//void main()
//{
//  //ifstream is("GoogleCodeJam/A-small-attempt0.in");
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


