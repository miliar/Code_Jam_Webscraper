#include<cstdio>
#include<map>
#include<stack>
#include<vector>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
vector<int>v;
int a[1001];
int rev(int n)
{
    int s=0,t;
    while(n>0)
    {
               t=n%10;
               s=s*10+t;
               n=n/10;
    }
    return s;
}


int main()
{
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int t,i,j,k=1;
	for(i=1;i<=1000;i++)
	{
    if(i==rev(i))
    {
     v.push_back(i);
     a[i]=1;
     }
     else
     a[i]=0;
     }
	for(i=0;i<v.size();i++)
	if(i*i<=1000 && a[i]==1&&a[i*i]==1 )
	a[i*i]=2;
    scanf("%d",&t);
	
    int r1,r2,count;
    while(t--)
	{
              scanf("%d%d",&r1,&r2);
              count=0;
              for(i=r1;i<=r2;i++)
              if(a[i]==2)
              {
                         count++;
              }
              printf("Case #%d: %d\n",k++,count);
              
              
    
     
     }
     
}

    
