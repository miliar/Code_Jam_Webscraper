//
//  main.cpp
//  Problem B. Cookie Clicker Alpha
//
//  Created by 朱 翼 on 14-4-12.
//  Copyright (c) 2014年 朱 翼. All rights reserved.
//



#include <cstdio>
#include <cstring>

int main(){
    int t;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    int kase=1;
    double c,f,x;
    while(t--)
    {
        scanf("%lf%lf%lf",&c,&f,&x);
        double ans=x/2.;
        double sum=0;
        for(int i=0;;i++)
        {
            sum=sum+1./(2+i*f);
            double res=x/(2.+(i+1)*f)+c*sum;
            if(res<=ans)
            {
                ans=res;
            }
            else
            {
                break;
            }
        }
        printf("Case #%d: %.7lf\n",kase++,ans);
    }
    return 0;
}
