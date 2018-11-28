#include <string>
#include <map>
#include <math.h>
#include <sstream>
#include <time.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

#define fx first
#define sx second

typedef pair<int,int> ii;
typedef vector<int> vec;
typedef vector<ii> vecp;
typedef long long int lli;
typedef unsigned long long int ulli;

bool func(int x, int r, int c)
{
  if(r>c)
  {
    int t=r;
    r=c;
    c=t;
  }
    // cout<<x<<" "<<r<<" "<<c<<endl;

  if((r*c)%x>0) return false;
  if(x==1) return true;
  if(x==2)
  { 
    if((r*c)%2==0) return true;
    else return false;
  }
  if(x==3)
  {
    if(r==1) return false;
    if(r==2)
    {
      if(c==2 || c==4) return false;
      else return true;
    }
    if(r==3) return true;
    if(r==4) return false;
  }
  if(x==4)
  {
    if(r<=2) return false;
    if(r==3)
    {
      if(c==3) return false;
      if(c==4) return true;
    }
    if(r==4) return true;
  }
}

int main()
{
  ifstream input;
  input.open("d-small0.in",ios::in);
  ofstream out;
  out.open("d.out",ios::out);
  // ofstream out2;
  // out2.open("bb.out",ios::out);


  int count;
  input>>count;
  
  for (int i = 1; i <= count; ++i)
  {
    int x,r,c;
    input>>x>>r>>c;

    //printing the output
    out<<"Case #"<<i<<": ";
    if(func(x,r,c)) out<<"GABRIEL";
    else out<<"RICHARD";
    

    if(i<count) out<<endl;
  }

  return 0;
}
