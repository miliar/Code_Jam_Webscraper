#include<iostream>
#include<fstream>
#include<cmath>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
using namespace std;
bool IsPrime(long long n)
{
	if (n==1) return false;
	if (n%2==0) return false;
	int s = (int)sqrt((double)n);
	for (int i=3;i<=s+1;i++)
	{
	  if (n%i==0) return false;
	}
	return true;
}
long long F(long long a, int st)
{
   long long rez=0;
   int k=0;
   string s=to_string(static_cast<long long>(a));
   for (int i=s.length()-1; i>=0; i--)
   {
      rez+=(s[i]-'0')*pow((double)st,k);
	  k++;
   }
   return rez;
}
long long StrToLong(string s)
{
	int L=s.length(),k(0);
	long long rez(0);
	for (int i=s.length()-1; i>=0; i--)
	{
	   rez+=(s[i]-'0')*pow(10.0,k);
	   k++;
	}
	return rez;
}
long long Dal(long long a)
{
	for (long long i=2; i<=a/2+1; i++)
	{
	   if (a%i==0) return i;
	}
	return -1;
}

string DEC_BIN(long long x)
{
   string res="",res1="";
   long long d;
   long long digits[2]={0,1};
   while (x!=0)
	   {
         d = x % 2;
         res+=to_string(static_cast<long long>(digits[d]));
         x=(x-d)/2;
   }
   //cout <<"res= "<<res << endl;
   int L= res.length();
   for (int i=0;i<L;i++) res1+=res[L-i-1];
   return res1;
}



int main()
{
  /*int T;
  string A[101];
  ifstream f1;
  f1.open("input.txt");
  f1 >> T;
  for (int i=1; i<=T; i++) f1 >> A[i];
  f1.close();
  */
  string s1="1";
  string s3="1";
  string s,s2,s_dec;
  int A[11]={0},z(0);
  long long a=10000000000000,b,temp,temp_dal,step(0);
  //cout <<"aaa "<<DEC_BIN(9) << endl;
  ofstream f2;
  f2.open("output.txt");
  f2 << "Case #1:" << endl;
  while(1)
  {
    step++;
	s_dec=DEC_BIN(step);
	//cout << s_dec <<" " << atoi(s_dec.c_str()) << endl;
	a=10000000000000;
	a+=atoi(s_dec.c_str());

	s2=to_string(static_cast<long long>(a));
	s=s1+s2+s3;
	b=StrToLong(s.c_str());
	for (int i=0;i<11;i++) A[i]=0;
	for (int i=2;i<=10;i++)
	  {
	    temp=F(b,i);
		if (!IsPrime(temp))
		{
		   temp_dal = Dal(temp);
		   if (temp_dal!=-1) A[i]=temp_dal; 
		}
		  //if (!IsPrime(F(b, i)) && Dal(b)!=-1) A[i]=Dal(b);
		else break;
	  }
	if (A[10]!=0)
	{
	   f2 << b;
	   for (int j=2;j<=10;j++) f2 << " " << A[j];
	   f2 << endl;
	   z++;
	}
	//cout << b << endl;
	if (z==50) break;
  }

  /*ofstream f2;
  f2.open("output.txt");
  
  for (int i=1; i<=T; i++)
  {
	  //int L=A[i].length();
	  f2 << "Case #" << i <<": " << F(A[i]) << endl;
  }

  f2.close();*/
  return 0;
 }