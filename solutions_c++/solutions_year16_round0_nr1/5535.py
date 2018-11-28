#include<iostream>
#include<fstream>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;
long long F(long long a)
{
   string s;
   set<int> B;
   int k=0, t=a;
   while(1)
   {
    s=to_string(static_cast<long long>(a));
	for (int i=0;i<s.length();i++) B.insert(s[i]-'0');
	k++;
	if (B.size()==10) return a;
	if (k==1000000) return -1;
	a+=t;
   }
}
int main()
{
  int T;
  long long A[101],t;
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
	  if (A[i]==0||F(A[i])==-1) f2 << "Case #" << i <<": INSOMNIA" << endl;
	  else f2 << "Case #" << i <<": " << F(A[i]) << endl;
  }

  f2.close();
  return 0;
 }