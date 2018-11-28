#include<iostream>
#include<stdio.h>
#include<cmath>
using namespace std;
int main()
{
      freopen("C-small-attempt3.in","r",stdin);
      freopen("Output1.txt","w",stdout);

       long long int t,e=0;
       cin>>t;
       while(t--)
       {
              long long int m,n,cntr=0,digita,cntr1=0,i,j,p,x,l,z;
              bool signa=true;
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
                     for(int y=m-2;y>0;y--)
                     {
                            if(x%2==1)
                            k[y]=1;
                            else
                            k[y]=0;
                            x=x/2;
                     }
                     //cout<<"hi 1"<<" ";
                     cntr=0;
                     long long int d[9];
                     for(i=2;i<=10;i++)
                     {
                            signa=false;
                            digita=0;
                            for(j=m-1;j>=0;j--)
                            {
                                   if(k[j]==1)
                                   {
                                          digita=digita+pow(i,m-1-j);
                                   }
                            }
                            //cout<<digita<<" ";
                            l=2;
                            while(l<=sqrt(digita))
                            {
                                   if(digita%l==0)
                                   {
                                          cntr++;
                                          d[i-2]=l;
                                          break;
                                   }
                                   l++;
                            }
                            if(cntr==9)
                            {
                                   cout<<digita<<" ";
                                   for(int g=0;g<9;g++)
                                   cout<<d[g]<<" ";
                                   cout<<endl;
                                   cntr1++;
                                   //cout<<digita<<" "<<i<<" ";
                            }
                            if(cntr1==z)
                            {
                                   break;
                            }
                     }
                     if(cntr1==z)
                     break;
              }
       }
}
