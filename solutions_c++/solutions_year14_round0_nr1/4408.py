#include<cstdio>
int n,a,b,c,x,tink;
int r[2][10],cnt,keep;
int ans[111]= {0};
void magic(int rr)
{
    scanf("%d",&x);
    for(b=1; b<=4; b++)
    {
        for(c=1; c<=4; c++)
        {
            if(b!=x)  scanf("%d",&tink);
            else scanf("%d",&r[rr][c]);
        }
    }
}
int main()
{
    scanf("%d",&n);
    for(a=1; a<=n; a++)
    {
        magic(0);
        magic(1);
        cnt=0;
        for(b=1; b<=4; b++)
        {
            for(c=1; c<=4; c++)
            {
                if(r[0][b]==r[1][c])
                {
                    keep=r[0][b];
                    cnt++;
                }
            }
        }
        if(cnt==1) ans[a]=keep;
        else if(cnt==0) ans[a]=0;
        else ans[a]=-1;
    }
    for(a=1; a<=n; a++)
    {
        printf("Case #%d: ",a);
        if(ans[a]==-1) printf("Bad magician!\n");
        else if(ans[a]==0) printf("Volunteer cheated!\n");
        else printf("%d\n",ans[a]);
    }
    return 0;
}
