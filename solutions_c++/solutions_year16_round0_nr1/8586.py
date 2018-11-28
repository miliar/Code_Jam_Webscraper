#include<stdio.h>
int cnt;
bool chk[10];
void findDigit(int x)
{
    while(x>0)
    {
loop:
//        printf("%d -> %d\n",x,x%10);
        if(chk[x%10]==false)
            cnt++;
        chk[x%10]=true;
        if(x>=10&&x/10==0)
        {
            x/=10;
            goto loop;
        }
        x/=10;
    }
}
main()
{
    int mx=0,q,nq,a,i,j,k;
    scanf("%d",&nq);
    for(q=0;q<nq;q++)
    {
        scanf("%d",&a);
//        a=q;
        if(a==0)
        {
            printf("Case #%d: INSOMNIA\n",q+1);
            continue;
        }
        for(i=0;i<10;i++)
            chk[i]=false;
        cnt=0;
        i=a;
        while(cnt<10)
        {
            findDigit(i);
//            printf("%d cnt= %d: ",i,cnt);
//            for(j=0;j<10;j++)
//                if(chk[j])
//                    printf("%d ",j);
//            printf("\n");
            i+=a;
        }
        printf("Case #%d: %d\n",q+1,i-a);
//        if(i/a>mx)
//            mx=i/a;
//        if(i/a==73)
//        printf("%d -> %d\n",a,mx);
    }
//    printf("mx= %d",mx);
    return 0;
}
