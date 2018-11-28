#include <iostream>
#include <cstdio>
#include <set>

using namespace std;
#define LD long long int
set<LD> s;
int main()
{
    freopen("lll.txt","r",stdin);
    freopen("output.txt","w",stdout);
    LD n,a,m,nn;
     scanf("%lld",&nn);
     for(LD i=1;i<=nn;i++){
       scanf("%lld",&a);
       printf("Case #%lld: ",i);
       if(a==0){
        printf("INSOMNIA\n");
       }
       else{
       LD j=1;
       while(s.size()<10){
        m=a*j;
        n=m;
       while(m>0){
           s.insert(m%10);
           if(s.size()==10){
            break;
           }
           m/=10;
       }
       j++;
       }
       printf("%lld\n",n);
       }
       s.clear();
     }
    return 0;
}
