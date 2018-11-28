#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

#define LL long long
#define ULL unsigned long long
#define m_p make_pair
#define l_b lower_bound
#define p_b push_back
#define w1 first
#define w2 second
#define maxlongint 2147483647
#define biglongint 2139062143

PII cheng(PII a,PII b)
{
    PII s;
    s.w1=a.w1*b.w1;
    if (a.w2==1) s.w2=b.w2; else
    if (b.w2==1) s.w2=a.w2; else
    if (a.w2==b.w2) s.w2=1,s.w1*=-1; else
    {
        if ((a.w2==2)&&(b.w2==3)) s.w2=4;
        if ((a.w2==2)&&(b.w2==4)) s.w2=3,s.w1*=-1;
        if ((a.w2==3)&&(b.w2==2)) s.w2=4,s.w1*=-1;
        if ((a.w2==3)&&(b.w2==4)) s.w2=2;
        if ((a.w2==4)&&(b.w2==2)) s.w2=3;
        if ((a.w2==4)&&(b.w2==3)) s.w2=2,s.w1*=-1;
    }
    return s;

}

int TT,L,X,flag,a[10005];
PII cc,s1[10005],s2[10005];
char st[10005];

int main()
{
    //1=1 i=2 j=3 k=4

    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);

    scanf("%d",&TT);
    for (int gb=1;gb<=TT;gb++)
    {
        scanf("%d %d",&L,&X);
        scanf("%s",st);
        for (int i=1;i<=L;i++)
            if (st[i-1]=='i') a[i]=2; else
            if (st[i-1]=='j') a[i]=3; else a[i]=4;
        for (int i=L+1;i<=L*X;i++) a[i]=a[(i-1)%L+1];
        s1[0]=m_p(1,1);
        for (int i=1;i<=L*X;i++) s1[i]=cheng(s1[i-1],m_p(1,a[i]));
        s2[L*X+1]=m_p(1,1);
        for (int i=L*X;i>=1;i--) s2[i]=cheng(m_p(1,a[i]),s2[i+1]);
        flag=1;
        for (int i=1;i<=L*X;i++)
            if ((s1[i].w1==1)&&(s1[i].w2==2))
            {
                cc=m_p(1,1);
                for (int j=i+1;j<=L*X;j++)
                {
                    cc=cheng(cc,m_p(1,a[j]));
                    if ((cc.w1==1)&&(cc.w2==3)&&(s2[j+1].w1==1)&&(s2[j+1].w2==4))
                    {
                        flag=0;
                        break;
                    }
                }
                if (flag==0) break;
            }
        printf("Case #%d: ",gb);
        if (flag==0) printf("YES\n"); else printf("NO\n");
    }

    return 0;
}
