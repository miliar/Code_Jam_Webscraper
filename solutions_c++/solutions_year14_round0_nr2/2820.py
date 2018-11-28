#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;
int main()
{
    int i,t;
    scanf("%d",&t);
    double c,f,x,res,temp,sum,inc;
    inc=2;
    for(i=1;i<=t;i++){
        scanf("%Lf %Lf %Lf",&c,&f,&x);
        res=x/2;
        sum=c/2;
        for(inc=2+f;;inc+=f){
            temp=sum+x/inc;
            if(temp>res){
                break;
            }
            else{
                res=temp;
            }
            sum=sum+c/inc;
        }
        printf("Case #%d: %0.7Lf\n",i,res);
    }
    return 0;
}
