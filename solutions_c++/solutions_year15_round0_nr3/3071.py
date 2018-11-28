#include<cstdio>

// 0,i,j,k
int c[4][4] =
{
    0, 1, 2, 3,
    1, 0, 3, 2,
    2, 3, 0, 1,
    3, 2, 1, 0
};

int d[4][4] =
{
    0, 0, 0, 0,
    0, 1, 0, 1,
    0, 1, 1, 0,
    0, 0, 1, 1
};

struct pos
{
    int cc,dd;
    bool i()
    {
        return cc == 1 && dd == 0;
    }
    bool j()
    {
        return cc == 2 && dd == 0;
    }
    bool k()
    {
        return cc == 3 && dd == 0;
    }
};
void mul(pos&e, pos a, pos b)
{
    e.cc = c[a.cc][b.cc];
    e.dd = d[a.cc][b.cc]^a.dd^b.dd;
    //printf("<%d,%d>",e.cc,e.dd);
}

char ss[10010];
int use[10010];

int fun(int n)
{
    int i;
    pos now = {0,0};
    for(i=0;i<n&&now.i()==false;i++)
    {
        mul(now, now, pos{use[i],0});
    }
    if(i==n)return 0;
    now = {0,0};
    for(;i<n&&now.j()==false;i++)
    {
        mul(now, now, pos{use[i],0});
    }
    if(i==n)return 0;
    now = {0,0};
    for(;i<n;i++)
    {
        mul(now, now, pos{use[i],0});
    }
    return now.k();
}
int main()
{
    int ti;
    scanf("%d",&ti);
    for(int ca=1;ca<=ti;ca++)
    {
        int l,x;
        scanf("%d%d",&l,&x);
        scanf("%s",ss);
        int n = l*x;
        for(int i=0;i<x;i++)
        for(int j=0;j<l;j++)
        {
            use[i*l + j] = ss[j] - 'i' + 1;
        }
        printf("Case #%d: %s\n",ca, fun(n)?"YES":"NO");
    }
}

