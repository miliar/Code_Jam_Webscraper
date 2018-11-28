#include<bits/stdc++.h>
using namespace std;
int p;
void sum(int *param1,int x,int *param2, int y)
{
    int temp=0;

     for (int i=0;i<x;i++)
    {
        temp=param1[i]+param2[i]+temp;
        param1[i]=temp%10;
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
    ifstream fin ( "A-large.in" );
    ofstream fout ( "A-large.txt" );
    int t;
    int a[10000],result[10000] ;
        int n,i=0,w=0;
    int digits[10];
   fin>>t;
   // cout<<t<<endl;
    while(t--)
    {  w++;
       for (int i=0;i<10000;i++) a[i]=0;
       for(int e=0;e<10;e++) digits[e]=0;
       fin>>n;
      // cout<<n<<endl;
       if (n==0) {
                  //cout<< "Case #"<<w<<":"<<"INSOMNIA"<<endl;
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


         sum(result,p,a,m);

         for (int c=p-1;c>=0;c--)
            {
                for(int e=0;e<10;e++)
                 if (result[c]==e && digits[e]==0) digits[e]=1;
            }

            f=0;
           for(int e=0;e<10;e++)
             if (digits[e]==0) f=1;


     }
    // cout<< "Case #"<<w<<":";
     fout<< "Case #"<<w<<": ";
      for (int c=p-1;c>=0;c--)
          {
             fout<<result[c];
             result[c]=0;
          }
     fout<<endl;
    }

   return 0;
}
