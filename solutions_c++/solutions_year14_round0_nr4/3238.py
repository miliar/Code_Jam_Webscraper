#include <iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
   int t,w;
   float a[1001],b[1001],tmp;
   cin>>t;
   for(w=1;w<=t;w++)
   {
       int n,i,k,first,last,count=0,z,y,j;
       cin>>n;

       for(i=0;i<n;i++)
       {
           cin>>a[i];
       }
        for(i=0;i<n;i++)
       {
           cin>>b[i];
       }

       sort(a,a+n);
       sort(b,b+n);
       k=0;
       first=0;
       last=n-1;
       for(i=n-1;i>=0;i--)
       {
           tmp=a[i];
           if(tmp>b[last])
           {
               count++;
               first++;
               continue;
           }
           if(tmp<b[last])
           {

               last--;
               continue;
           }
       }
       z=count;


       //////////////////////////////////
       count=0;
       j=0;
       for(i=0;i<n;i++)
       {
           tmp=b[i];
           for(;j<n;j++)
           {
               if(a[j]>tmp)
               {
               count++;j++;
               break;
               }
           }
           if(j==n)
           break;
       }
       y=count;

       cout<<"Case #"<<w<<": "<<y<<" "<<z<<endl;

   }

   return 0;
}
