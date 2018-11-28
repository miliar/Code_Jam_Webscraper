# include <bits/stdc++.h>
using namespace std;
bool track[10];
int n;
bool flag=0;
int main(void)
{
    int test;
    scanf("%d",&test);
    int count=1;
    while(test--)
    {
        int digno=0;
        int n;
        scanf("%d",&n);
        bool flag=0;
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",count);
            count++;
            continue;
        }
        long long temp=n;long long dup=n;
        while(1)
        {
            while(temp!=0)
            {
                if(track[temp%10]==0)
                {
                    track[temp%10]=1;
                    digno++;
                }
                temp=temp/10;
                if(digno==10)
                {
                    flag=1;
                    break;
                }
            }
            if(!flag)
            {
                temp=dup+n;
                dup=temp;
            }
            else
                break;
        }
        printf("Case #%d: %lld\n",count,dup);
        count++;
        for(int i=0;i<10;i++)
            track[i]=0;
    }
    return 0;
}
