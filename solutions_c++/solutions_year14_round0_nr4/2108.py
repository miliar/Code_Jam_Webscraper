#include<iostream>
#include<fstream>


using namespace std;
fstream f1,f2;



int main()
{  f1.open("large.in",ios::in);
   f2.open("out.out",ios::out);
   int cas,count=0,n,p;
   double a[1000],b[1000],key;
   int t,m,i,j,k,flag;
   f1>>cas;
   while(cas)
   {   t=0;
       m=0;
       flag=0;
       cas--;
       count++;
       f1>>n;
       for(i=0;i<n;i++)
        f1>>a[i];
       for(i=0;i<n;i++)
        f1>>b[i];
       for(j=1;j<n;j++)
       {
           key=a[j];
           k=j-1;
           while(k>=0&&a[k]>key)
           {
               a[k+1]=a[k];
               k=k-1;
           }
           a[k+1]=key;
       }
              for(j=1;j<n;j++)
       {
           key=b[j];
           k=j-1;
           while(k>=0&&b[k]>key)
           {
               b[k+1]=b[k];
               k=k-1;
           }
           b[k+1]=key;
       }

       for(i=0;i<n;i++)
       {
           for(j=t;j<n;j++)
           {
               if(a[i]<b[j])
               {
                   t=j+1;
                   break;
               }
               else
               m++;
           }

           if(j>=n)
           break;
       }

       i=0;
       j=0;
       p=0;
       for(i=0;i<n;i++)
       {
           if(a[i]<b[p])
           {

              a[i]=-1;



           }
           else
           p++;

       }
       for(i=0;i<n;i++)
       {
           if(a[i]>=0)
           flag++;
       }

       f2<<"Case #"<<count<<": "<<flag<<" "<<m<<"\n";






   }
   return 0;
}
