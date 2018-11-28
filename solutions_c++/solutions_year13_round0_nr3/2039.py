#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int checkpal(int a[],int n);
int main()
{
  int t,i,k,a[20];
  int count,c1,c2,num;
  std::ifstream iff("V:/C-large-1.in");
  std::ofstream off("V:/output.txt");
  iff>>t;
  long long int inp[t][2],b[40],sq,j,l;
  int o[t];
  for(i=0;i<t;i++)
  {
    iff>>inp[i][0]>>inp[i][1];
  }
  count=0;
  for(j=1;j<=10000000;j++)
    {
      c1=0;
      c2=0;
      k=0;
            l=j;
            do
            {
                a[k]=l%10;
                l=l/10;
                k++;
            }
            while(l>0);
      		c2=checkpal(a,k);
      if(c2==1)
      {
        sq=j*j;
        k=0;
      	l=sq;
        do
      	{
           	a[k]=l%10;
           	l=l/10;
           	k++;
      	}
      	while(l>0);
      	c1=checkpal(a,k);
      	if(c1==1)
        {
            b[count]=sq;
            count++;
        }
      }
    }

  for(i=0;i<t;i++)
  {
      num=0;
      for(k=0;k<count;k++)
      {
        if((b[k]>=inp[i][0])&&(b[k]<=inp[i][1]))
            {//cout<<"t ";
            num++;}
      }
    off<<"Case #"<<i+1<<": "<<num<<endl;
  }
  return 0;
}

int checkpal(int a[],int n)
{
  int i,j,flag=1;
  for(i=0;i<(n/2);i++)
    if(a[i]!=a[n-i-1])
    	flag=0;
  return flag;
}
