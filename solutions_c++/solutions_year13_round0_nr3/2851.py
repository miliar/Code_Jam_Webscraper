#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

bool pan(unsigned __int64 x)
{
 unsigned __int64 temp=x;
 unsigned __int64 b=0;
 while(temp>0)
 {
  b*=10;
  b+=(temp%10);
  temp/=10; 
 }
 if(b==x) return true;
 else return false;
}

int main()
{
  ifstream inf("C-large1.in");
  ofstream outf("C-large1.out");
  int k;
  inf>>k;
  for(int q=1;q<=k;q++)
  {
  unsigned __int64 n,m;
  inf>>n>>m;
  int sum=0;
  for(unsigned __int64 i=ceil(sqrt(n));i<=floor(sqrt(m));i++)
   if((pan(i))&&(pan(i*i))) sum++;
  outf<<"Case #"<<q<<": "<<sum;
  outf<<endl;
  }
  inf.close();
  outf.close();
  return 0;
}
