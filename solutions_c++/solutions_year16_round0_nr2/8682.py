#include<stdio.h>
main()
{
    int cnt,q,nq,i,j,k;
    char str[1000],cur=0;
    scanf("%d",&nq);
    for(q=0;q<nq;q++)
    {
        scanf("%s",&str);
        cnt=0;
        cur=0;
        for(i=0;str[i]!='\0';i++)
        {
            if(cur!=str[i])
            {
                cur=str[i];
                cnt++;
            }
        }
//        printf("%d\n",cnt);
        if(cur=='+')
            cnt--;
        printf("Case #%d: %d\n",q+1,cnt);
    }
    return 0;
}
