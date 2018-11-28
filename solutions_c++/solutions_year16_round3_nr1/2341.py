#include<bits/stdc++.h>
using namespace std;
int a[20];
int main()
{
//    freopen("A small input.in","r",stdin);
//    freopen("A small output.out","w",stdout);
    freopen("A large input.in","r",stdin);
    freopen("A large output.out","w",stdout);
    int t,ti,m,i,j,k,x,sum=0,mx,mem,cnt1,cnt2;
    scanf("%d",&t);
    for(ti=1;ti<=t;ti++)
    {
        printf("Case #%d: ",ti);
        sum=0;
        scanf("%d",&m);
        for(i=0;i<m;i++)
        {
            scanf("%d",&a[i]);
            sum+=a[i];
        }
        while(sum)
        {
            cnt1=0;
            cnt2=0;
            for(i=0,mx=0;i<m;i++)
                if(a[i]>mx)
                {
                    mx=a[i];
                    mem=i;
                }
            for(i=0;i<m;i++)
            {
                if(a[i]>(sum-1)/2)
                    cnt1++;
            }
            for(i=0;i<m;i++)
            {
                if(a[i]>(sum-2)/2)
                    cnt2++;
            }
            if(cnt2==1)
            {
                for(i=0;i<m;i++)
                    if(a[i]>(sum-2)/2)
                    {
                        printf("%c ",'A'+i);
                        a[i]--;
                        sum--;
                        break;
                    }
            }
            else if(cnt2==2)
            {
                for(i=0;i<m;i++)
                    if(a[i]>(sum-2)/2)
                    {
                        printf("%c",'A'+i);
                        a[i]--;
                        sum--;
                        break;
                    }
                for(i=0;i<m;i++)
                    if(a[i]>(sum-1)/2)
                    {
                        printf("%c ",'A'+i);
                        a[i]--;
                        sum--;
                        break;
                    }
            }
            else
            {
                printf("%c ",'A'+mem);
                a[mem]--;
                sum--;
            }
        }
        printf("\n");
    }
}
