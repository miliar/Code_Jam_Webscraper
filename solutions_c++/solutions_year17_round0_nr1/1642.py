#include <iostream>
#include <string>
#define N 10
using namespace std;

string S;
int K;
int rst;

void read()
{
  cin >> S >> K;
}

void flip(int x)
{
  rst++;
  for(int i=x;i<x+K;i++)
    S[i]='+'+'-'-S[i];
}

bool solve()
{
  rst=0;
  for(int k=0;k<S.size()-K+1;k++)
    {
      if(S[k]=='-')
	flip(k);
    }
  for(int k=S.size()-K+1;k<S.size();k++)
    if(S[k]=='-')
      return false;
  return true;
}


int main()
{
  int T;
  cin >> T;
  for(int t=1;t<=T;t++)
    {
      read();
      cout << "Case #"<< t <<": ";
      if(solve())
	cout << rst;
      else
	cout << "IMPOSSIBLE";
      cout << endl;
    }
  return 0;
}
