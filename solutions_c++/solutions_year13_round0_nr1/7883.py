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
#define max(a,b)    (((a) > (b)) ? (a) : (b))
#define min(a,b)    (((a) < (b)) ? (a) : (b))
#define sqr(a)    ((a)*(a))

//////////////////////////////////////////////////////////////////////////

char a[4][4];

char win(int i, int j, int di, int dj)
{
  {
    bool win_0 = true;
    for (int k=0;k<4;++k)
      if (a[i+di*k][j+dj*k]!='O'&&a[i+di*k][j+dj*k]!='T')
      {
        win_0=false;
        break;
      }
      if (win_0)
        return 'O';
  }

  {
    bool win_1 = true;
    for (int k=0;k<4;++k)
      if (a[i+di*k][j+dj*k]!='X'&&a[i+di*k][j+dj*k]!='T')
      {
        win_1=false;
        break;
      }
      if (win_1)
        return 'X';
  }

  return 0;
}

void main()
{
  ifstream is("a.in");
  ofstream os("a.out");

  int t;
  is>>t;

  for (int ti=0;ti<t;++ti)
  {
    //solve
    bool compl=true;
    for (int i=0;i<4;++i)
      for (int j=0;j<4;++j)
      {
        is>>a[i][j];
        if (a[i][j]=='.')
          compl=false;
      }


    char win_=0;

    for (int i=0;i<4;++i)
    {
      int win_h = win(i,0,0,1);
      int win_v = win(0,i,1,0);

      if (win_h)
      {
        //os << "Case #"<<ti+1<<": " << win_h << " won\n";
        win_ = win_h;
        break;
      }
      if (win_v)
      {
        win_ = win_v;
        //os << "Case #"<<ti+1<<": " << win_v << " won\n";
        break;
      }
    }

    if (!win_)
    {
      win_=win(0,0,1,1);
    }

    if (!win_)
    {
      win_=win(0,3,1,-1);
    }

    if (!win_)
    {
      os << "Case #"<<ti+1<<": " << (compl?"Draw":"Game has not completed") << "\n";
        

    }
    else
    {
      os << "Case #"<<ti+1<<": " << win_ << " won\n";
    }

    //os << "Case #"<<ti+1<<": ";
    //out
    //os<<"\n";
  }
}

//void main()
//{
//  ifstream is("a.in");
//  ofstream os("a.out");
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


