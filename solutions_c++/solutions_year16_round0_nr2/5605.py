#include<iostream>
#include<fstream>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;
int F(string s)
{
	int L = s.length();
	int A[101];
	if (s[0]=='-') A[1]=1;
	else if (s[0]=='+') A[1]=0;
	
	if (L==1) return A[1];
	
	if (s[1]=='-'&&s[0]=='-') A[2]=A[1];
	else if (s[1]=='-'&&s[0]=='+') A[2]=A[1]+2;
	else if (s[1]=='+'&&s[0]=='+') A[2]=A[1];
	else if (s[1]=='+'&&s[0]=='-') A[2]=A[1];

	if (L==2) return A[2];

	for (int i=3;i<=L;i++)
	{
	  if (s[i-1]=='-'&&s[i-2]=='-')      A[i]=A[i-1];
	  else if (s[i-1]=='-'&&s[i-2]=='+') A[i]=A[i-1]+2;
	  else if (s[i-1]=='+'&&s[i-2]=='+') A[i]=A[i-1];
	  else if (s[i-1]=='+'&&s[i-2]=='-') A[i]=A[i-1];
	}
	return A[L];
}
int main()
{
  int T;
  string A[101];
  ifstream f1;
  f1.open("input.txt");
  f1 >> T;
  for (int i=1; i<=T; i++) f1 >> A[i];
  f1.close();
  
  
  //cout << "aaa" << s1 << endl;
  ofstream f2;
  f2.open("output.txt");
  
  for (int i=1; i<=T; i++)
  {
	  //int L=A[i].length();
	  f2 << "Case #" << i <<": " << F(A[i]) << endl;
  }

  f2.close();
  return 0;
 }