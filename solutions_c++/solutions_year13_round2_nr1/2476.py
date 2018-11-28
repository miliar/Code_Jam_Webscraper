#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
using namespace std;
int a[1000005];
int main()
{
 int t,n,i,j,mt,c,cas,d,c1;
 scanf("%d",&t);
 for(cas=1;cas<=t;cas++)
 {
           scanf("%d%d",&mt,&n);
           c1=0;
           for(i=0;i<n;i++)
           {
                           scanf("%d",&a[i]);
                           if(a[i]<mt)
                           c1++;
           }
           sort(a,a+n);
           c=0;i=0;
           int f=0,pos=0;
           while(i<n)
           {
                           if(a[i]<mt)
                           {mt+=a[i];i++;}
                           else
                           {
                               d=(a[i]-mt)+1;
                               if(d<mt)
                               {
                                       if(d>mt-1)
                                       {mt+=d;i++;}
                                       else
                                       mt+=mt-1;
                                       c++;
                               }
                               else if(d>=mt)
                               {
                                    f++;
                                    if(f==1)
                                    pos=i;
                                    if(mt>1  && i<n-1)
                                    {mt+=mt-1;i=pos;}
                                    
                                    
                                    else
                                    i++;
                               c++;
                               
                               }
                               else
                               i++;
                           }
                         //  cout<<i<<" "<<mt<<endl;
                                   
           }
           if(c1==0)
           c=min(c,n);
           cout<<"Case #"<<cas<<": "<<c<<endl;
 } 
                               
           
           
return 0;
}
