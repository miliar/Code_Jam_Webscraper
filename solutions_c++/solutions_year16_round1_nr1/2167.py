/*#include<stdio.h>
int n, arr[1010], ans, x[1010];
bool chk[1010], c;
void back(int num)
{
    int i, xx, yy;
    if(num==ans)
    {
        for(i=1; i<=ans; ++i)
        {
            if(i==ans) xx=1;
            else xx=i+1;

            if(i==1) yy=ans;
            else yy=i-1;

            if(arr[x[i]]==x[xx] || arr[x[i]]==x[yy]) continue;
            else break;
        }
        if(i<=ans) return;
        c=true;
        return;
    }
    ++num;
    if(c==true) return;
    for(i=1; i<=n; ++i)
    {
        if(chk[i]) continue;
        chk[i]=true;
        x[num]=i;
        back(num);
        chk[i]=false;
        x[num]=0;
    }
    return;
}
int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt","w", stdout);
    int i, j, T, tt;
    scanf("%d", &T);
    for(tt=1; tt<=T; ++tt)
    {
        scanf("%d", &n);
        for(i=1; i<=n; ++i)
        {
            scanf("%d", &arr[i]);
        }
        c=false;
        for(ans=n; ans>=1; --ans)
        {
            back(0);
            if(c==true) break;
        }
        printf("Case #%d: %d\n", tt, ans);
    }
}
*/
#include <stdio.h>
#include <string.h>

typedef struct data
{
    char arr[1010];
    char mdf[1010];
};

int main ()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, i, k, l;
    char tmp[1010];

    struct data in[110];

    scanf("%d", &T);

    for(i=0;i<T;i++)
    {
        scanf("%s", in[i].arr);

        in[i].mdf[0]=in[i].arr[0];

        for(l=0;l<1000;l++)
            tmp[l]=0;

        for(k=1;k<strlen(in[i].arr);k++)
        {
            if(in[i].arr[k]>=in[i].mdf[0])
            {
                strcpy(tmp, in[i].mdf);
                strcpy(in[i].mdf+1, tmp);
                in[i].mdf[0]=in[i].arr[k];
            }
            else
                in[i].mdf[k]=in[i].arr[k];
        }

        printf("Case #%d: %s\n", i+1, in[i].mdf);
    }

    return 0;
}
