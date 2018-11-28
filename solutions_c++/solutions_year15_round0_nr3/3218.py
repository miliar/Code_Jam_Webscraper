#include <cstdio>
#include <cstring>
#include <vector>
#include <cstdlib>
using namespace std;

const int N = 5, g[N][N]={{0,0,0,0,0},
                          {0,1,2,3,4},
                          {0,2,-1,4,-3},
                          {0,3,-4,-1,2},
                          {0,4,3,-2,-1}},
                 s[N][N]={{0,1,1,1,1},
                          {0,1,-1,1,-1},
                          {0,1,-1,-1,1},
                          {0,1,1,-1,-1}},
                inv[N]  ={0,1,-2,-3,-4};
const int maxl =10025;
int T,X,L,n;
char a[maxl];
int m1[maxl],m2[maxl];
vector<int> p1,p2;

int sgn(int x)
{
    return x<0?-1:1;
}

int abs(int x)
{
    return x<0?-x:x;
}

#define mul(x,y) sgn(x)*sgn(y)*g[abs(x)][abs(y)]

void pre1()
{
    int c=1;
    for(int i = 0; i < n;i++)
    {
        c=mul(c,a[i]);
        m1[i]=c;
        if(c==2)
            p1.push_back(i);
    }
}

void pre2()
{
    int c=1;
    for(int i = n-1; i >= 0;i--)
    {
        c=mul(a[i],c);
        m2[i]=c;
        if(c==4)
            p2.push_back(i);
    }
}

bool check(int l, int r)
{
    int x=m1[l-1], y=m1[r], invx=sgn(x)*inv[abs(x)], v=mul(invx,y);
    //printf("x=%d y=%d invx=%d v=%d\n",x,y,invx,v);
    return v==3;
}

int main()
{
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);

    scanf("%d",&T);

    for(int t0=1;t0<=T;t0++){
        memset(a,0,sizeof(a));
        p1.clear();
        p2.clear();

        scanf("%d%d",&L,&X);
        n=L*X;
        scanf("%s",a);

        //printf("n=%d a=%s\n",n,a);

        for(int i=0;a[i];i++)
            a[i]=a[i]-'i'+2;

        int p=L;
        for(int i=1;i<X;i++)
            for(int j=0;j<L;j++)
                a[p++]=a[j];

        pre1();
        pre2();
/*
        printf("m1=");
        for(int i = 0; i < L; i++)
            printf("%d ", m1[i]);
        printf("\n");

        printf("m2=");
        for(int i = 0; i < L; i++)
            printf("%d ", m2[i]);
        printf("\n");
*/
        bool ok=false;
/*
        printf("p2=");
        for(int i = 0; i<p2.size();i++)
            printf("%d ",p2[i]);
*/
        for(int i = 0; i < p1.size(); i++)
            for(int j = 0; j < p2.size(); j++)
                if(p1[i]<p2[j]-1){
                    if(check(p1[i]+1,p2[j]-1)){
                        ok = true;
                        goto print;
                    }
                }
                else{
                    break;
                }
        print:
        if(ok)
            printf("Case #%d: YES\n",t0);
        else
            printf("Case #%d: NO\n",t0);
    }
}
