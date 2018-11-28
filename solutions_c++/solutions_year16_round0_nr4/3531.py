#include<fstream>
#include<iostream>
#include<cmath>
using namespace std;
int main()
{
 long power,res,t,i,k,c,s,j,power1;
 ifstream input;
 ofstream output;
 input.open("input4.txt");
 output.open("output4.txt");
 input>>t;
 for(i=1;i<=t;i++)
 {
  input>>k;input>>c;input>>s;output<<"Case #"<<i<<": ";
  if(s<k){output<<"IMPOSSIBLE"<<endl;continue;}
  power = pow(k,c);power1=power/k;
  for(j=1;j<=k;j++)
  {
   output<<power-j*power1+1<<" ";
  }
  output<<endl;
 }
 return 0;
}
