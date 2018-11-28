#include<cstdio>
#include<cstdlib>
int main()
{
    int t,a,b,c,k,i,j,cnt,l;
    scanf("%d",&t);
    for(l=0;l<t;l++)
    {
        cnt=0;
        scanf("%d %d %d",&a,&b,&k);
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                c=i&j;
                if(c<k)
                    cnt++;
            }
        }
        printf("Case #%d: %d\n",l+1,cnt);
    }
}
