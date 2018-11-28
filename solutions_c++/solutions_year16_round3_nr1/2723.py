#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,u,max2,n,m,a[30],max1,x,sum;
    scanf("%d",&t);
     vector<string>v;
    for(u=1;u<=t;u++)
    {
       v.clear();
        cin>>x;
        sum=0;
        max1=0;
        for(i=0;i<x;i++)
        {
            cin>>a[i];
        if(a[i]>max1){
            max1=a[i];
            m=i;
        }
        sum=sum+a[i];
        }
        max2=0;

        string s;
        char p;
   for(i=0;i<x;i++)
   {
       if(a[i]>max2 && i!=m)
       {
           max2=a[i];
           n=i;
       }
   }
      if(a[m]==a[n] && a[m]==1 && x==2)
   {
       p=m+'A';
       s=s+p;
       p=n+'A';
       s=s+p;
       sum=sum-2;
       a[m]=a[m]-1;
       a[n]=a[n]-1;
       v.push_back(s);
   }
   else
   if(a[m]==a[n] && a[m]!=1)
   {
       p=m+'A';
       s=s+p;
       p=n+'A';
       s=s+p;
       sum=sum-2;
       a[m]=a[m]-1;
       a[n]=a[n]-1;
       v.push_back(s);
   }
   else
   {
       p=m+'A';
       s=s+p;
       a[m]=a[m]-1;
       sum=sum-1;
       v.push_back(s);
   }
        while(sum>2)
        {
            max1=0;
    max2=0;
            for(i=0;i<x;i++)
            {
                if(a[i]>max1)
            {
                max1=a[i];
                m=i;
            }
            }
            s="";
       for(i=0;i<x;i++)
   {
       if(a[i]>max2 && i!=m)
       {
           max2=a[i];
           n=i;
       }
   }
   if(a[m]==a[n] && a[m]!=1)
   {
       p=m+'A';
       s=s+p;
       p=n+'A';
       s=s+p;
       a[m]=a[m]-1;
       a[n]=a[n]-1;
       sum=sum-2;
       v.push_back(s);
   }
   else
   {
       p=m+'A';
       s=s+p;
       a[m]=a[m]-1;
       sum=sum-1;
       v.push_back(s);
   }
        }
     //   cout<<"out"<<"\n";
        s="";
        for(i=0;i<x;i++)
        {
            if(a[i]==1)
            {
             p=i+'A';
             s=s+p;
             a[i]=a[i]-1;
            }
        }
        v.push_back(s);
        printf("Case #%d: ",u);
        for(i=0;i<v.size();i++)
        {
            cout<<v[i]<<" ";
        }
     //   cout<<v[n-2]<<v[n-1];
        cout<<"\n";
    }
    return 0;
}
