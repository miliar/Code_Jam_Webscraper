#include<iostream.h>
#include<fstream.h>
#include<math.h>

ifstream fin("ghi.txt");
ofstream fout("ans.txt");

int pal(int a)
{
 int b[10],i=0,temp,k=0,m=0;
 while(a>=10)
 {
  b[i]=a%10;
  a=a/10;
  i++;
 }
 b[i]=a;
 m=i;
 for(int j=0;j<=i/2;j++,i--)
 {
  temp=b[j];
  b[j]=b[i];
  b[i]=temp;
 }
 for(j=0;j<=m/2;j++,m--)
 {
  if(b[j]!=b[m])
   k=1;
  }
  if(k==0)
  return 1;
  else
  return 0;

}


void check(int x,int y,int e)
{
 int l,count=0;
 int p=sqrt(x);
 int q=sqrt(y);
 float z;
 for(int i=x;i<=y;i++)
 {
  l=pal(i);
  if(l==1)
  {
   z=sqrt(i);
   for(int j=p;j<=q;j++)
   {
    if(z==j)
    {
     l=pal(z);
     if(l==1)
      count++;
     break;
    }
   }
  }
 }
 fout<<"Case #"<<e+1<<": "<<count<<"\n";
}





void main()
{
 int a,b,n;
 fin>>n;
 for(int j=0;j<n;j++)
 {
  fin>>a;
  fin>>b;
  check(a,b,j);
 }
}