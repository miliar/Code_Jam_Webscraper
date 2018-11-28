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
typedef long long     ll;
typedef unsigned int  UInt;
#define FOR(i,a,b)    for(int i=a;i<(int)b;++i)
#define FOR_D(i,a,b)  for(int i=a;i>=b;--i)
template<class T> inline T   sqr(T v)  { return v * v; }
template<class T> inline int sign(T v) { return v == 0 ? 0 : (v > 0 ? 1 : -1); }
template<class T> int get_bit(T v, int bit_index) { return (v >> bit_index) & 1; } //return {0,1}


//a - ���� ���������������� �� �����-�� �����. ����������� ���-��, ��� ������ � 0 ����������, � ��������� ������ ����� ���-�. it_max=70 ��� n<=10^6
//b - �� ���� ����� � big �����
//c - ����� ����������� �� ������ ������� ���������: ���� �� �������� � ������������
//d - ����� �����

//////////////////////////////////////////////////////////////////////////

//d
void main()
{
  //ifstream is("GoogleCodeJam/D-small-attempt0.in");
  ifstream is("GoogleCodeJam/D-large.in");
  //ifstream is("GoogleCodeJam/input.txt");
  ofstream os("GoogleCodeJam/output.txt");

  int t;
  is>>t;

  for (int ti=0;ti<t;++ti)
  {
    int k,c,s;
    is>>k>>c>>s;

    os << "Case #"<<ti+1<<": ";

    if (k>s*c)
      os<<"IMPOSSIBLE\n";
    else
    {
      for (int i=0; i<k; )
      {
        ll n=0;
        for (int j=0; j<c; ++j, ++i)
        {
          n=n*k+min(i,k-1);
        }
        os<<n+1<<" ";
      }
      os<<"\n";
    }
  }
}

////c
//void main()
//{
//  //ifstream is("GoogleCodeJam/C-small-attempt0.in");
//  //ifstream is("GoogleCodeJam/C-large.in");
//  ifstream is("GoogleCodeJam/input.txt");
//  ofstream os("GoogleCodeJam/output.txt");
//
//  const int N = 1000000; //�� ������ ����� ������ ~75000 ������� ��� 640000
//  int lp[N+1]; //lp[i] - ����������� ������� �������� ��� i; ���-��, ��� ������ ��������� 0
//  vector<int> pr; //������� ����� � ������������� ���������
//  {
//    memset(lp,0,sizeof lp);
//    for (int i=2; i<=N; ++i) {
//      if (lp[i] == 0) { //=> i � �������, �.�. ��� ���� �� ������������ ������ ���������
//        lp[i] = i;
//        pr.push_back (i);
//      }
//      for (int j=0; j<(int)pr.size() && pr[j]<=lp[i] && i*pr[j]<=N; ++j)
//        lp[i * pr[j]] = pr[j]; //������� ���������� ����� 1 ��� ��������� � lp[x]
//    }
//  }
//
//  int t;
//  is>>t;
//
//  for (int ti=0;ti<t;++ti)
//  {
//    int n,j;
//    is>>n>>j;
//
//    os << "Case #"<<ti+1<<": ";
//    os<<"\n";
//
//    int divisors[11];
//    for (UInt mask=0; j; ++mask)
//    {
//      int bit_hi=30;
//      for (; bit_hi>=0 && !get_bit(mask,bit_hi); --bit_hi);
//
//      int base=2;
//      for (; base<=10; ++base)
//      {
//        bool ok=false;
//        FOR (i,0,pr.size())
//        {
//          int p = pr[i];
//
//          {
//            bool ok=true;
//            ll num=1, k=base;
//            for (int i = 0;i<n-2;++i,k*=base)
//            {
//              if (k>p)
//                ok=false;
//              if (get_bit(mask,i))
//                num+=k;
//              if (num>p)
//                ok=false;
//            }
//            num+=k;
//            if (num>p)
//              ok=false;
//
//            if (ok&&num==p)
//              continue;
//          }
//
//          ll r = 1;
//          {
//            ll r1=1;
//            for (int i=n-1;i;--i)
//            {
//              r1*=base;
//              r1%=p;
//            }
//            r+=r1;
//            r%=p;
//          }
//
//          {
//            ll r1=1;
//            for (int i=0; i<=bit_hi; ++i)
//            {
//              r1*=base;
//              r1%=p;
//
//              if (get_bit(mask,i))
//              {
//                r+=r1;
//                r%=p;
//              }
//            }
//          }
//
//          if (!r)
//          {
//            divisors[base]=p;
//            ok=true;
//            break;
//          }
//        }
//        if (!ok)
//          break;
//      }
//
//      if (base>10) //ok
//      {
//        os<<"1";
//        for (int i = n-3; i>=0; --i)
//          os<<get_bit(mask,i);
//        os<<"1 ";
//
//        FOR (i,2,11)
//          os<<divisors[i]<<" ";
//        os<<endl;
//        --j;
//
//        ////!!!!!check
//        //for (int base=2; base<=10; ++base)
//        //{
//        //  ll num=1, k=base;
//        //  for (int i = 0;i<n-2;++i,k*=base)
//        //    if (get_bit(mask,i))
//        //      num+=k;
//        //  num+=k;
//
//        //  os<<num<<" ";
//
//        //  if (num%divisors[base])
//        //    os<<"error"<<endl;
//        //}
//        //os<<endl;
//      }
//    }
//  }
//}

////a
//void main()
//{
//  ifstream is("GoogleCodeJam/A-large.in");
//  //ifstream is("GoogleCodeJam/input.txt");
//  ofstream os("GoogleCodeJam/output.txt");
//
//  int t;
//  is>>t;
//
//  for (int ti=0;ti<t;++ti)
//  {
//    ll n;
//    is>>n;
//
//    int it_max=0;
//    //for (n=1;n<=1000000;++n)
//    {
//      vector<int> use(10,0);
//      int use_k=0;
//      ll nn=n;
//
//      for (int it=0;it<100000;++it,nn+=n)
//      {
//        for (ll k=nn;;)
//        {
//          if (!use[k%10])
//          {
//            use[k%10]=1;
//            ++use_k;
//          }
//          k/=10;
//          if (!k)
//            break;
//        }
//        if (use_k==10)
//          break;
//        it_max=max(it_max,it);
//      }
//
//      os << "Case #"<<ti+1<<": ";
//      //os << "Case #"<<n<<": ";
//      use_k==10? os<<nn : os<<"INSOMNIA";
//      os<<"\n";
//    }
//
//    //cout<<"it_max = "<<it_max<<endl;
//  }
//}

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
//  //ifstream is("GoogleCodeJam/B-small-attempt0.in");
//  ifstream is("GoogleCodeJam/B-large.in");
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


