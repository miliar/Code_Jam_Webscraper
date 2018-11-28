#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
long long int min1[110],s,i,ans,n;
                       long long int game(long long int s,long long i,long long count)
                       {
                       if(i==n)
                       return count;
                       if(min1[i]<s)
                       return game(s+min1[i],i+1,count);

                              else
                              {
                              return min(game(s+s-1,i,count+1),game(s,i+1,count+1));
                              }
                              return ans;
                              }
int main()
{

     freopen("C:\\Users\\DELL\\Desktop\\input.txt","r",stdin); 
freopen("C:\\Users\\DELL\\Desktop\\output.txt","w",stdout);
            long long int t,f=1;
            scanf("%lld",&t);
            for(f=1;f<=t;f++)
            {
            scanf("%lld %lld",&s,&n);
            for(i=0;i<n;i++)
            scanf("%lld",&min1[i]);
            sort(min1,min1+n);
            if(s==1)
            printf("Case #%lld: %lld\n",f,n);
            else
            printf("Case #%lld: %lld\n",f,game(s,0,0));

            }
//system("pause");
return 0;
}
