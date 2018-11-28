#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

bool pan(int x)
{
 int temp=x;
 int b=0;
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
  ifstream inf("C-small.in");
  ofstream outf("C-small.out");
  int k;
  inf>>k;
  for(int q=1;q<=k;q++)
  {
  int n,m;
  inf>>n>>m;
  int sum=0;
  for(int i=ceil(sqrt(n));i<=floor(sqrt(m));i++)
   if((pan(i))&&(pan(i*i))) sum++;
  outf<<"Case #"<<q<<": "<<sum;
  outf<<endl;
  }
  inf.close();
  outf.close();
  return 0;
}
