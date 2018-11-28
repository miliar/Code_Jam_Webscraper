#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
using namespace std;

int S[10]['Z'-'A'+1];

int C['Z'-'A'+1];

void read()
{
  for(int i=0;i<='Z'-'A';i++)
    C[i]=0;
  string str;
  cin >> str;
  for(int i=0;i<str.size();i++)
    C[str[i]-'A']++;
}

string solve(int n,int arr['Z'-'A'+1])
{
  bool done=true;
  for(int i=0;i<='Z'-'A';i++)
    if(arr[i]<0)
      return "X";
    else if(arr[i]>0)
      done=false;
  if(done)
    return "";
  if(n==10)
    return "X";
  int arr1['Z'-'A'+1];
  int arr2['Z'-'A'+1];
  for(int i=0;i<='Z'-'A';i++)
    arr1[i]=arr2[i]=arr[i];
  for(int i=0;i<='Z'-'A';i++)
    arr1[i]-=S[n][i];
  string rst1 = solve(n,arr1);
  string rst2 = solve(n+1,arr2);
  if(rst1.compare("X")!=0)
    {
      string rst=to_string(n);
      rst+=rst1;
      return rst;
    }
  if(rst2.compare("X")!=0)
    {
      return rst2;
    }
  return "X";
}

string solve()
{
  return solve(0,C);
}

int main()
{
  int T;
  string arr[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
  for(int i=0;i<10;i++)
    {
      for(int j=0;j<arr[i].size();j++)
	S[i][arr[i][j]-'A']++;
    }
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
