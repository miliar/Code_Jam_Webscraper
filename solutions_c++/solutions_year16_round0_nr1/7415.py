#include<bits/stdc++.h>
using namespace std;
int p;
void sumofNo(int *param1,int x,int *param2, int y)
{
    int temp=0;
     for (int j=0;j<x;j++)
    {
        temp=param1[j]+param2[j]+temp;
        param1[j]=temp%10;
        temp=temp/10;
    }
   while (temp>0)
     {
         param1[x++]=temp%10;
          temp=temp/10;
     }
     p=x;
 }

int main()
{
   ifstream fin ( "C:/Users/6030777/Desktop/input.txt" );
   ofstream fout ( "C:/Users/6030777/Desktop/output.txt" );
    int t;
    int a[10000],output[10000] ;
    int n,i=0,w=0;
    int digits[10];
   fin>>t;
    while(t--)
    {  w++;
       for (int i=0;i<10000;i++) a[i]=0;
       for(int e=0;e<10;e++) digits[e]=0;
       fin>>n;
             if (n==0) {
                           fout<< "Case #"<<w<<": "<<"INSOMNIA"<<endl;continue;
                  }

       int m=0;
       while(n>0)
       {
           a[m++]=n%10;
           n=n/10;
       }
       p=m;
       int f=1;

       while(f)
     {
         sumofNo(output,p,a,m);
         for (int c=p-1;c>=0;c--)
            {
                for(int e=0;e<10;e++)
                 if (output[c]==e && digits[e]==0) digits[e]=1;
            }

            f=0;
           for(int e=0;e<10;e++)
             if (digits[e]==0) f=1;

     }
        fout<< "Case #"<<w<<": ";
        for (int c=p-1;c>=0;c--)
          {
             fout<<output[c];
             output[c]=0;
          }
     fout<<endl;
    }

   return 0;
}
