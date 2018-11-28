#include<stdio.h>
#include<iostream>
#include<fstream>
using namespace std;
main()
{
      float x,n;
      int i,m,j,t,A,B,count;
      ifstream ifile("e:/ip.txt");
      ofstream ofile("e:/op.txt");
      ifile>>t;
      for (j=1;j<=t;j++)
      {
          ifile>>A>>B;
          count=0;
          for (m=A;m<=B;m++)
          {
              float squareroot(float);
              char palno(int);
              n=m;
              x=squareroot(n);
              i=x;
              if ((i*i)==n)
              {
                   if (palno(m)=='y')
                   {
                                     if (palno(i)=='y')
                                     {
                                                       count++;
                                     }
                   }
              }
          }
      ofile<<"Case #"<<j<<": "<<count<<endl;
      }
}
float squareroot(float num) 
{
      if(num >= 0) 
      { 
       float x = num; 
       int i; 
       for(i = 0; i < 40; i ++) 
       x = (((x * x) + num) / (2 * x)); 
       return x; 
      }
} 
 char palno(int n1)
{
     int x,p,r,i,sum,a,m,z;
     char c;
     m=n1;
     i=0;
     while (n1!=0)
     {
           n1=n1/10;
           i++;
     }
     int b[i];
     for (z=i-1;z>=0;z--)
     {
         b[z]=m%10;
         m=m/10;               
     }
     p=0;
     for (x=0;x<=((i/2)-1);x++)
     {
         if (b[x]==b[i-1-x])
         p++;
     }
     if ((p-1)==((i/2)-1))
     {
                          c='y';
     }
     else
     {
         c='n';
     }
     return c;
}     
