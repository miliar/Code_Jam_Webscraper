#include<iostream>
#include<vector>
using namespace std;
vector<long long int> arr;
int palin(long long int v)
{
    int temp[20],k=0,i;
    while(v>0)
    {
       temp[k]=v%10;
       v=v/10;
       k++;
    }
    for(i=0;i<k;i++)
      if(temp[i]!=temp[k-i-1])
         return 0;
    return 1;
}
void init()
{
     long long int i,val;
     long long int lim=1,t=10;
     for(i=1;i<=14;i++)
        lim=lim*t;
     for(i=1;(i*i)<=lim;i++)
     {
         if(palin(i))
         {
            val=i*i;
            if(palin(val))
            {
              // printf("%lld %lld\n",i,val);
               arr.push_back(val);
            }
         }
     }
}            
int main()
{
    freopen("infair.txt","r",stdin);
    freopen("outfair.txt","w",stdout);
    init();
    int tc,t,i;
    scanf("%d",&t);
    for(tc=1;tc<=t;tc++)
    {
        long long int a,b;
        scanf("%lld%lld",&a,&b);
        int ans=0;
        for(i=0;i<arr.size();i++)
           if(arr[i]>=a && arr[i]<=b) ans++;
        printf("Case #%d: %d\n",tc,ans);
    }
}
