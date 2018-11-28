#include <stdio.h>
#include<string.h>
int main()
{
    FILE *fp=freopen("/Users/rohansuri/Documents/datastructures/datastructures/B-large.in","r",stdin);
    if(fp==NULL)printf("yo");
    freopen("/Users/rohansuri/Documents/datastructures/datastructures/AO.out","w",stdout);
    double c,f,x,ans,prev,p,tmp;int T,t;
    scanf("%d",&T);
    for(t=0;t<T;t++)
    {   tmp=0.0;
        scanf("%lf%lf%lf",&c,&f,&x);
        p=2;
        prev=x/p;
        while(1)
        {   ans=prev;
            tmp+=c/p;
            p+=f; 
            prev=tmp + x/p;
            //printf("tmp %lf\n",tmp);
            if(ans<prev)break;
        }
        printf("Case #%d: %lf\n",t+1,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}