#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
bool myfunc(float i,float j)
{
    return(i<j);
}
 vector<float>a;
 vector<float>b;
 vector<float>c;
int upper_bnd(float val)
{
   int pos;
   int mid;
   int i=0;
   int h=c.size();
   while(i<h)
   {
       if(c[i]>val)
        return i;
     i++;
   }    
    return -1;
}
int main()
{
    int t,n,k,i,j,up,cnt,cnt2;
    float x;
    cin>>t;
    k=1;
    
    while(k<=t)
    {
       cin>>n;
       a.clear();
       b.clear();
       c.clear();
       for(i=0;i<n;i++)
       {
          cin>>x;
          a.push_back(x);
       }
       for(i=0;i<n;i++)
       {
          cin>>x;
          b.push_back(x);
          c.push_back(x);
       }
       cnt=0;
       sort(a.begin(),a.end(),myfunc);
       sort(b.begin(),b.end(),myfunc);
       sort(c.begin(),c.end(),myfunc);
       vector<float>::iterator it;
       vector<float>::iterator it1=b.begin();
       for(vector<float>::iterator it=a.begin();it!=a.end();it++)
       {
         if((*it)<(*it1))
          {
              b.pop_back(); 
          } 
          else 
          {
                 cnt++;
                if(it1!=b.end())
                  it1++;     
          }                         
       }
       cnt2=0;
       
       for(it=a.begin();it!=a.end();it++)
       {
          float v=(*it);
          int up=upper_bnd(v);
          if(up==-1)
          {
              break;
          }
          else
          {
             c.erase(c.begin()+up);
          }                   
       }
       while(it!=a.end())
       {
          cnt2++;
          it++;                  
       }
       cout<<"Case #"<<k<<": "<<cnt<<" "<<cnt2<<"\n";
       k++;           
    }
   return 0;   
}
