
#include<stdio.h>

int T;

int main()
{
    scanf("%d",&T);
    int S,n,counter,res;
    char c;
    for(int i=0;i<T;i++)
    {
        scanf("%d",&S);
        counter=0;
        res=0;
        for(int j=0;j<=S;j++)
        {
            do{scanf("%c",&c);}while(c<'0' || c>'9');
            n=c-'0';
            if(counter<j && n){
                res+=j-counter;
                counter=j;
            }
            counter+=n;
        }
        printf("Case #%d: %d\n",i+1,res);
    }
    return 0;
}

