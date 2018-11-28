#include<iostream>
#include<string.h>
#include<stdio.h>
#include<vector>
using namespace std;
vector<long long>vec;
bool is(long long x)
{
     int p[20];
     p[0]=0;
     while (x)
     {
         p[++p[0]]=x%10;
         x/=10;
     }
     for (int i = 1; i <=p[0]/2; i++)
     if(p[i]!=p[p[0]-i+1]) return false;
     return true;
}
int main()
{
    int i,j,k,n,m,cs,t=0;
    long long a,b;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C.txt","w",stdout); 
    scanf("%d",&cs);
    for (long long i = 1; i <= 999999; i++)
    {
        if (is(i) && is (i*i))
        {vec.push_back(i*i);
   
        }
        
    }
    
    while (t++ < cs)
    {
          m=0;
          cin>>a>>b;
          for (int i = 0; i <vec.size(); i++)
          if (vec[i]>=a&&vec[i]<=b)
          m++;
          printf("Case #%d: %d\n",t,m);
      
    }    
}
