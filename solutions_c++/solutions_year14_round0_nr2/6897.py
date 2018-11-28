#include <iostream>
#include <cstdio>
#include <cstdlib>
#define ll long long int

#define in(a,b,c) scanf("%Lf %Lf %Lf",&a,&b,&c);
#define in_(a) scanf("%d",&a);
using namespace std;

int main() {
   int t,k=0,i;
   long double c,f,x,ans[100],mi,sum,prev,upto,ok;
    in_(t);
    while(t--){
        in(c,f,x);
        i=1;
        mi=x/(2.0);
        prev=mi;
        upto = mi;
        sum=prev;
	ok=sum;
	//printf(" %lf ->",sum);
        while(sum<=ok){
	    ok=sum;
            sum+=c/(2.0+(i-1)*f);
            sum-=prev;
            prev=x/(2.0+i*f);
            sum+=prev;
            if(sum<mi)mi=sum;
            //printf(" %lf ->",sum);
            i++;
        }
        ans[k]=mi;
        k++;
    }
    for(int j=0;j<k;j++){
        printf("Case #%d: %0.7Lf\n",j+1,ans[j]);
    }
    return 0;
}
