#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<set>
#include<utility>
using namespace std;
int main()
{
    FILE *fp,*fo;
    fp=fopen("D-large.in","r");
    fo=fopen("output.txt","w");
    int t,n,num1,num2,ans2,ans1,count=0,i,type;
    pair<float,int> mypair;
    set<pair<float,int> > myset;
    set<pair<float,int> >::reverse_iterator it;
    fscanf(fp,"%d",&t);
    float key;
    while(t--)
    {
        count++;
         fscanf(fp,"%d",&n);
         for(i=0;i<2*n;i++)
         {
             fscanf(fp,"%f",&key);
             mypair.first=key;
             if(i<n)
             {
             mypair.second=1;

             }
             else
             {
             mypair.second=2;

             }
             myset.insert(mypair);
         }
         it=myset.rbegin();
         type=(*it).second;
         while(it!=myset.rend()&&type==2)
         {
             it++;
             if(it==myset.rend())
                break;
             type=(*it).second;
         }
         ans2=0,num1=0,num2=0;
         while(it!=myset.rend())
         {
             if(type==1)
             {
                 num1++;
             }
             else
             {
                 if(num1>0)
                 {
                     ans2++;
                     num1--;
                 }
             }
             it++;
              if(it==myset.rend())
                break;
            type=(*it).second;
         }
         ans1=0,num1=0,num2=0;
         it=myset.rbegin();
         type=(*it).second;
         while(it!=myset.rend()&&type==1)
         {
             it++;
             if(it==myset.rend())
                break;
             type=(*it).second;
         }
          while(it!=myset.rend())
         {
             if(type==2)
             {
                 num2++;
             }
             else
             {
                 if(num2>0)
                 {
                     ans1++;
                     num2--;
                 }
             }
             it++;
              if(it==myset.rend())
                break;
            type=(*it).second;
         }
         fprintf(fo,"%s%d%s%d%s%d\n","Case #",count,": ",ans2," ",n-ans1);
         //printf("%d %d\n",ans2,n-ans1);
         myset.clear();
    }
    return 0;
}
