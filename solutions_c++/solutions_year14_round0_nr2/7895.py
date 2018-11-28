#include<cstdio>
#include<iostream>

using namespace std;

double sol,C,F,X,time,tralala;
int i,j,T,test;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);

    for(test=1; test<=T; test++)
    {
        cin>>C>>F>>X;
        sol=100000;
        for(i=0; i<=X; i++)
        {
            time=0;
            if(i>=1) tralala+=C/(2+(i-1)*F);
            else tralala=0;
            time=tralala+X/(2+i*F);
            if(time>sol) break;
            sol=time;
        }
        printf("Case #%d: %.8f\n",test,sol);
    }

    return 0;
}
