#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
       freopen("A-large.in","r",stdin);
       freopen("Output1.txt","w",stdout);
       long long int t,l=0;
       cin>>t;
       while(t--)
       {
              long long int n,i,m=0,k,x,p;
              cin>>n;
              l++;
              if(n==0)
              {
                     cout<<"Case #"<<l<<": INSOMNIA"<<endl;
                     continue;
              }
              bool a[10],c;
              for(i=0;i<10;i++)
              a[i]=false;
              while(1)
              {
                     c=true;
                     p=n*(m);
                     m++;
                     k=n*m;
                     for(i=0;i<10;i++)
                     {
                            if(a[i]==false)
                            c=false;

                     }
                     if(c==true)
                     break;
                     while(k!=0)
                     {
                          x=k%10;
                          a[x]=true;
                          k=k/10;
                     }


              }
              cout<<"Case #"<<l<<": "<<p<<endl;
       }
}
