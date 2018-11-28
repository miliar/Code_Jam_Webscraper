#include <iostream>
#include <stdio.h>
using namespace std;

int t;
int n;

int seq[100111];
int L=0;
int ctr[3];

int beat[3]={1,2,0};
char symbol[3]={'P','R','S'};

void Generate(int level,int mv)
{
    if (level==n)
    {
        ctr[mv]++;

        L++;
        seq[L]=mv;

        return;
    }

    Generate(level+1,mv);
    Generate(level+1,beat[mv]);

    return;
}

int helper[100111];

void SWAP(int l1,int r1,int l2,int r2)
{
    int i;
    int uk=0;

    for (i=l1;i<=r1;i++)
    {
        uk++;
        helper[uk]=seq[i];

        seq[i]=seq[l2+i-l1];
    }

    uk=0;
    for (i=l2;i<=r2;i++)
    {
        uk++;
        seq[i]=helper[uk];
    }

    return;
}

void SortSeq(int l,int r)
{
    if (l+1==r)
    {
        if (seq[l]>seq[r])
        SWAP(l,l,r,r);

        return;
    }

    int mid=(l+r)/2;
    bool needswap=false;
    int i;

    SortSeq(l,mid);
    SortSeq(mid+1,r);

    for (i=l;i<=mid;i++)
    {
        if (seq[i]<seq[mid+i-l+1])
        {
            needswap=false;
            break;
        }
        else if (seq[i]>seq[mid+i-l+1])
        {
            needswap=true;
            break;
        }
    }

    if (needswap)
    SWAP(l,mid,mid+1,r);

    return;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int test;
    int i;
    int R,P,S;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        scanf("%d",&n);
        scanf("%d %d %d",&R,&P,&S);

        for (i=0;i<=2;i++)
        {
            ctr[0]=0;
            ctr[1]=0;
            ctr[2]=0;
            L=0;

            Generate(0,i);

            if (ctr[0]==P && ctr[1]==R && ctr[2]==S)
            {
                break;
            }
        }

        printf("Case #%d: ",test);

        if (i==3)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }

        SortSeq(1,L);

        for (i=1;i<=L;i++)
        {
            printf("%c",symbol[ seq[i] ]);
        }
        printf("\n");
    }

    return 0;
}
