#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#define LL long long int
using namespace std;

int N,R,P,S;

void read()
{
  cin >> N >> R >> P >> S;
}

char winner(int r,int p,int s)
{
  if(r+p+s==2)
    {
      if(r==1 && p==1)
	return 'P';
      else if(r==1 && s==1)
	return 'R';
      else if(p==1 && s==1)
	return 'S';
      else
	return ' ';
    }
  if(r+p<s || r+s<p || p+s<r)
    return ' ';
  int p1 = (p+r-s)/2; // PR
  int s1 = (p+s-r)/2; // PS
  int r1 = (r+s-p)/2; // RS
  return winner(r1,p1,s1);
}

string solve()
{
  char rst = winner(R,P,S);
  if(rst == ' ')
    return "IMPOSSIBLE";
  vector<string> R;
  vector<string> P;
  vector<string> S;
  for(int i=0;i<=N;i++)
    {
      R.push_back("");
      P.push_back("");
      S.push_back("");
    }
  R[0]="R";
  P[0]="P";
  S[0]="S";
  for(int n=1;n<=N;n++)
    {
      string r1 = R[n-1]+S[n-1];
      string r2 = S[n-1]+R[n-1];
      if(r1.compare(r2)<0)
        R[n]=r1;
      else
	R[n]=r2;
      
      string p1 = R[n-1]+P[n-1];
      string p2 = P[n-1]+R[n-1];
      if(p1.compare(p2)<0)
        P[n]=p1;
      else
	P[n]=p2;

      string s1 = P[n-1]+S[n-1];
      string s2 = S[n-1]+P[n-1];
      if(s1.compare(s2)<0)
        S[n]=s1;
      else
	S[n]=s2;
    }
  if(rst=='R')
    return R[N];
  else if(rst=='P')
    return P[N];
  else
    return S[N];
}

int main()
{
  int T;
  cin >> T;
  for(int t=1;t<=T;t++)
    {
      read();
      cout << "Case #" << t << ": ";
      cout << solve();
      cout << endl;
    }
  return 0;
}
