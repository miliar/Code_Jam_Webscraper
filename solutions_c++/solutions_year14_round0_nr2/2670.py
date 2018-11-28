#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int N,t;
    double cur,ans,c,f,x,spent,spentt;
    
    scanf("%d",&N);
    for(t=1;t<=N;t++){
        scanf("%lf %lf %lf",&c,&f,&x);
        cur=0;
        spent=0;
        spentt=0;
        for(;;){
            spent+=c/(2+cur*f);
            if(x/(2+f*cur)+spentt < x/(2+(cur+1)*f)+spent)break;
            else{
                spentt+=c/(2+cur*f);
                cur+=1;
            } 
        }
        ans=x/(2+f*cur)+spentt;
        printf("Case #%d: %.7lf\n",t,ans);
    }
       
    return 0;
}
