#include <iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
   int T,x;
   scanf("%d",&T);
   for(x=1;x<=T;x++)
   {
       int N,i,k,strt,end,Naomi=0,z,y,j;
       scanf("%d",&N);
       float a[N],b[N],tmp;
       for(i=0;i<N;i++)
       {
           scanf("%f",&a[i]);
       }
        for(i=0;i<N;i++)
       {
           scanf("%f",&b[i]);
       }
       
       sort(a,a+N);
       sort(b,b+N);
       k=0;strt=0;end=N-1;
       for(i=N-1;i>=0;i--)
       {
           tmp=a[i];
           if(tmp>b[end])
           {
               Naomi++;
               strt++; 
               continue;
           }
           if(tmp<b[end])
           {
              // Ken++;
               end--;
               continue;
           }
       }
       z=Naomi;
      
       
       //////////////////////////////////
       Naomi=0;
       j=0;
       for(i=0;i<N;i++)
       {
           tmp=b[i];
           for(;j<N;j++)
           {
               if(a[j]>tmp)
               {
               Naomi++;j++;
               break;
               }
           }
           if(j==N)
           break;
       }
       y=Naomi;
       
       cout<<"Case #"<<x<<": "<<y<<" "<<z<<endl;
       
   }
   
   return 0;
}

