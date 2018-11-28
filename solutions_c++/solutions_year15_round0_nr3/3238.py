#include<bits/stdc++.h>

using namespace std;
char a[20000];
char z[20000];
int mul[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int change(char x)
{
    if(x=='i')
        return 2;
    else if(x=='j')
        return 3;
    else
        return 4;
}
int main()
{
    int t,l,x,i,sign,tsign,len,k,flag1,flag2,flag0,n;
    int ans=0;
    char b,c;
    k=0;
    scanf("%d",&t);
    while(t--)
    {
        k++;
        scanf("%d%d",&l,&x);
        scanf("%s",&z);
        n=l*x;
        for(i=0;i<n;i++)
            a[i]=z[i%l];
        ans=1;
        flag0=0;
        flag1=0;
        flag2=0;
        for(i=0;i<n;i++)
        {
            if(ans>0)
                ans=mul[ans][change(a[i])];
            else
                ans=(-1)*mul[abs(ans)][change(a[i])];
            if(ans==2&&(!flag0)&&(!flag1)&&(!flag2))
            {
                flag0=1;
                ans=1;
            }
            if(ans==3&&(flag0)&&(!flag1)&&(!flag2))
            {
                flag1=1;
                ans=1;
            }
            if(ans==4&&(flag0)&&(flag1)&&(!flag2)&&i==n-1)
            {
                flag2=1;
            }
        }
//        printf("%d%d%d\n",flag0,flag1,flag2);
        if(flag0&&flag1&&flag2)
            printf("Case #%d: YES\n",k);
        else
            printf("Case #%d: NO\n",k);
    }
    return 0;
}
