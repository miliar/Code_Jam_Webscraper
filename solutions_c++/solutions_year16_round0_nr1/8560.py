#include<iostream>
#include<stdio.h> 
long long int N,B,A;
using namespace std;
main()
{
      FILE *fp;
      fp=fopen("out2.txt","w");
      int T,flag,i,j,sum,c;
      bool a[10];
      cin>>T;
      c=T;
      while(T--)
      {
                flag=0;
             memset(a, true, sizeof(a));
             cin>>N;
             A=N;
             if(N==0)
             fprintf(fp,"Case #%d: INSOMNIA\n",(c-T));
             else
             {
                 for(N,i=1;flag!=1;N=i*A)
                 {
                                 B=N;
                                 sum=0;
                                 while(B)
                                 {
                                         a[B%10]= false;
                                         B=B/10;
                                 }
                                 i++;
                                 for(j=0;j<10;j++)
                                 {
                                                  if(a[j]== false)
                                                  sum++;
                                                  if(sum==10)
                                                  flag=1;
                                 }
                 }
                 fprintf(fp,"Case #%d: %d\n",(c-T),(N-A));
             }
      }
             return 0;
}
