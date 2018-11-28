#include<iostream>
#include<stdio.h>
#include<cmath>
using namespace std;
int main()
{
      freopen("C-small-attempt1.in","r",stdin);
      freopen("Output1.txt","w",stdout);

       long long int y,t,e=0;
       cin>>t;
       while(t--)
       {
              long long int m,n,res1=0,numa,res2=0,i,j,p,x,l,z;
              bool depa=true;
              cin>>m>>n;
              e++;
              z=n;
              long long int k[m];
              cout<<"Case #"<<e<<":"<<endl;
              for(p=pow(2,m-1);p<pow(2,m);p++)
              {
                     x=p;
                     k[m-1]=1;
                     k[0]=1;
                     y=m-2;
                     while(y>0)
                     {
                            if(x%2==1)
                            k[y]=1;
                            else
                            k[y]=0;
                            x=x/2;
                            y--;
                     }
                     //cout<<"hi 1"<<" ";
                     res1=0;
                     long long int d[9];
                     for(i=2;i<=10;i++)
                     {
                            depa=false;
                            numa=0;
                            for(j=m-1;j>=0;j--)
                            {
                                   if(k[j]==1)
                                   {
                                          numa=numa+pow(i,m-1-j);
                                   }
                            }
                            //cout<<numa<<" ";
                            l=2;
                            while(l<=sqrt(numa))
                            {
                                   if(numa%l==0)
                                   {
                                          res1++;
                                          d[i-2]=l;
                                          break;
                                   }
                                   l++;
                            }
                            if(res1==9)
                            {
                                   cout<<numa<<" ";
                                   for(int g=0;g<9;g++)
                                   cout<<d[g]<<" ";
                                   cout<<endl;
                                   res2++;
                                   //cout<<numa<<" "<<i<<" ";
                            }
                            if(res2==z)
                            {
                                   break;
                            }
                     }
                     if(res2==z)
                     break;
              }
       }
}
