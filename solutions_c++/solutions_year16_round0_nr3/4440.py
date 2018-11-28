#include<iostream>
#include<stdio.h>
#include<cmath>
using namespace std;
int main()
{
       freopen("C-small-attempt0.in","r",stdin);
       freopen("Output1.txt","w",stdout);

       long long int t;
       cin>>t;
       while(t--)
       {
              long long int m,n,count=0,number,count2=0,i,j,p,x,l,z,e=0;
              bool flag=true,flag1=false,flag2=false;
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
                     count=0;
                     long long int d[9];
                     for(i=2;i<=10;i++)
                     {
                            flag=false;
                            number=0;
                            for(j=m-1;j>=0;j--)
                            {
                                   if(k[j]==1)
                                   {
                                          number=number+pow(i,m-1-j);
                                   }
                            }
                            //cout<<number<<" ";
                            for(l=2;l<=sqrt(number);l++)
                            {
                                   if(number%l==0)
                                   {
                                          count++;
                                          d[i-2]=l;
                                          break;
                                   }
                            }
                            if(count==9)
                            {
                                   cout<<number<<" ";
                                   for(int g=0;g<9;g++)
                                   cout<<d[g]<<" ";
                                   cout<<endl;
                                   count2++;
                                   //cout<<number<<" "<<i<<" ";
                            }
                            if(count2==z)
                            {
                                   break;
                            }
                     }
                     if(count2==z)
                     break;
              }
       }
}
