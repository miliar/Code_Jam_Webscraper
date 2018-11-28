#include<cstdio>

int sti(char x)
{
    return (int)x-'0';
}

int t,n,cnt,id,ad;
char s[1005];

int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("out_large.txt","w",stdout);
    scanf("%d",&t);
    for(int z=0;z<t;z++)
    {
        scanf("%d%s",&n,s);
        ad=id=cnt=0;
        while(id!=n)
        {
            cnt+=sti(s[id++]);
            if(id>cnt)
            {
                ad++;
                cnt++;
            }
        }
        printf("Case #%d: %d\n",z+1,ad);
    }
    return 0;
}
