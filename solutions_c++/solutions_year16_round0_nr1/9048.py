#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
int t,i=1;
ifstream in("input.txt");
ofstream out("output.txt");
in>>t;
for(i=1;i<=t;i++)
{
    int n,c=1,j=2,check[10],p;
    for (int o=0;o<10;o++)
        check[o]=0;
    in>>n;
    p=n;
if(n!=0)
while(c)
{
    int temp=n,k,sum=0;
for (; temp> 0; temp /= 10){
check[temp%10]=1;
}
  for(k=0;k<10;k++)
  {

      sum=sum+check[k];
      if(sum==10)
      {
        c=0;
      out<<"Case #"<<i<<": "<<n<<endl;
      }
  }
 // printf("%d\n",n);
n=j*p;
j++;
}
else
    out<<"Case #"<<i<<": "<<"INSOMNIA\n";
}
    return 0;
}
