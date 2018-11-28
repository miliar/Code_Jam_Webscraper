#include<iostream>
using namespace std;
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cases;
    scanf("%d",&cases);
    int t =0;
    while(cases--)
    {
                  t++;
  long long   int i,j,k;
    scanf("%lld %lld %lld",&i,&j,&k);
    long long int ct = 0;
    for(int s= 0;s<i;s++)
    {
            for(int e=0;e<j;e++)
            {
        long long     int ans =  s&e;
            if(ans<k)
            {
                     ct++;
            }
            }
            
    }
    printf("Case #%d: %d\n",t,ct);//'<<endl;
   }
    
    return 0;
    
}
