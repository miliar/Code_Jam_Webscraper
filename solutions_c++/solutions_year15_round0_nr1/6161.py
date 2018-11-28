#include<cstdio>
int main()
{
    int t,s,i,j,res,total;
    char arr[2000];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        total=0;
        scanf("%d %s",&s,arr);
        res=0;
        for(j=0;j<=s;j++)
        {
            if(arr[j]!='0')
            {
                if(total<j)
                {
                    res=res+j-total;
                    total=j;
                }
            }
            total=total+arr[j]-'0';
        }
        printf("Case #%d: %d\n",i,res);
    }
    return 0;
}
