
#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
#define ll long long int
using namespace std;
 int main()
 {
   ll t,n;
   ll a[n];
   char p[n];
   char alpha[26];
   ll i,j;
   for(i=0;i<26;i++)
   alpha[i]=(char)('A'+(i));
   ll count =0;
   cin>>t;
   ll x=0;
   while(t--)
   {
       x++;
       cout<<"Case #"<<x<<": ";
       cin>>n;
       count =0;
       for(i=0;i<n;i++)
       {cin>>a[i];
       count+=a[i];
       p[i]=alpha[i];
       }

       while(count >0)
       {
           ll f=0;
           for(i=0;i<n-1;i++)
           {
               if(a[i]<a[i+1])
               {f=1;break;}
           }

        if(f)
        {
       for(i=0;i<n-1;i++)
       {
           for(j=0;j<n-i-1;j++)
           {
               if(a[j]<a[j+1])
               {
                   ll temp=a[j];
                   a[j]=a[j+1];
                   a[j+1]=temp;
                   char t=p[j];
                   p[j]=p[j+1];
                   p[j+1]=t;
               }
           }
       }
        }

       if(a[0]>1 && a[1]>1)
       {
           cout<<p[0]<<p[1]<<' ';
           a[0]--;a[1]--;
            count-=2;
       }
       else if(a[0]==1 && a[1]==1 && count==2)
       {
           cout<<p[0]<<p[1]<<' ';
           a[0]--;a[1]--;
           count-=2;
       }
       else if(a[0]>1 && a[1]==1 && count==2)
       {
           if(a[0]>2)
           {cout<<p[0]<<p[0]<<' ';
           a[0]-=2;
           count-=2;

           }
           else
           {
               cout<<p[0]<<' ';
               a[0]--;
               count--;
           }
       }
       else if(a[0]>1 && a[1]==1)
       {
           if(count-a[0]==1)
           {
               cout<<p[0]<<' ';
               a[0]--;
               count--;
           }
           else
           {
               cout<<p[0]<<p[0]<<' ';
               a[0]-=2;
               count-=2;
           }
       }
       else if(a[0]==1)
       {
           ll co=0;
           for(j=0;j<n;j++)
           {
               if(a[j]==1)
               co++;
               else
               break;
           }

           if(co==3)
           {cout<<p[0]<<' ';
           a[0]--;
           count--;}
           else if(co>3)
           {
               cout<<p[0]<<p[1]<<' ';
               a[0]--;a[1]--;
               count-=2;
           }
       }

       }
       cout<<endl;
   }
    return 0;
 }
