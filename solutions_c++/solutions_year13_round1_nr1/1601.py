#include<cstdio>
#include<limits.h>
#include<string>
#include<vector>
#include<iostream>
#include<cstdlib>
#include<math.h>
#include<algorithm>
using namespace std;
int main()
{
     freopen("A-small-attempt0.in","r",stdin);
  freopen("output.txt","w",stdout);
  int t,z=0;
  scanf("%d",&t);
  while(t--)
{
            z++;
            int r,x,flag=0,count=0;
            long long int cost1,cost2,cost;
            cin>>r>>x;
            while(!flag)
            {
                        cost1=r*r;
                        cost2=(r+1)*(r+1);
                        cost=cost2-cost1;
                        r=r+2;
                        x=x-cost;
                        if(x>=0)
                        count++;
                        else
                        flag=1;
            }
            cout<<"Case #"<<z<<": "<<count<<endl;
  }
  return 0;
}
            

                        
