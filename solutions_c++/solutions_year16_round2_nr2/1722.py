#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

string C,J;
int L;

void read()
{
  cin >> C >> J;
  L=C.size();
  int A = 3-L;
  int B = 3-L;
  for(int i=0;i<A;i++)
    C="0"+C;
  for(int i=0;i<B;i++)
    J="0"+J;
}

int D(int a,int b)
{
  int d = a-b;
  if(d<0)
    d=-d;
  int X[3];
  int Y[3];
  for(int i=0;i<3;i++)
    {
      X[2-i]=a%10;
      Y[2-i]=b%10;
      a/=10;
      b/=10;
    }
  for(int i=0;i<3;i++)
    if((C[i]!='?' && (C[i]-'0')!=X[i]) || (J[i]!='?' && (J[i]-'0')!=Y[i]))
      return 1000;
  return d;
}

void solve()
{
  int d = 10000;
  int a=5432534;
  int b=654354;
  for(int i=0;i<1000;i++)
    for(int j=0;j<1000;j++)
      {
	int tmp = D(i,j);
	if(tmp<d)
	  {
	    d=tmp;
	    a=i;
	    b=j;
	  }
	else if(tmp==d &&(i<a || (i==a && j<b)))
	  {
	    a=i;
	    b=j;
	  }
      }
  C=to_string(a);
  J=to_string(b);
  int A = L-C.size();
  int B = L-J.size();
  for(int i=0;i<A;i++)
    C="0"+C;
  for(int i=0;i<B;i++)
    J="0"+J;
}

int main()
{
  int T;
  cin >> T;
  for(int t=1;t<=T;t++)
    {
      read();
      cout << "Case #" << t << ": ";
      solve();
      cout << C << " " << J;
      cout << endl;
    }
  return 0;
}
