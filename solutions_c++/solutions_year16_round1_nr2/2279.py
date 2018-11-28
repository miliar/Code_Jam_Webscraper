#include<iostream>
#include<cmath>
#include<string>
#include<cstdlib>
#include<cstring>
using namespace std;

int height[2502];
int N;
int ans[55],ansn,maxn=0;

void calculate()
{
   ansn=0;

   for(int i=0;i<=maxn;i++)
   {
       if(height[i]%2!=0)
       {
           ans[ansn++]=i;
       }
   }

   for(int i=0;i<ansn;i++)
   {
       cout<<" "<<ans[i];
   }
   cout<<endl;
}

int main()
{
    int n,temp;
    cin>>n;

    for(int i=1;i<=n;i++)
    {
       cin>>N;
       cout<<"Case #"<<i<<":";
       memset(height,0,sizeof(height));

        maxn=0;

        for(int j=0;j<2*N-1;j++)
        {
           for(int k=0;k<N;k++)
           {
               cin>>temp;
               height[temp]++;

               if(temp>maxn)
                maxn=temp;

           }
        }

       calculate();

    }

    return 0;
}
