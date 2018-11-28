#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
using namespace std;

typedef __int64 LL;

typedef struct
{
    LL num;
    LL d[9];
}Record;
vector<Record> v;
void eval(LL value)
{
    vector<int> c;
    LL tmp[9];
    LL N=value;
    while (N>0)
    {
        c.push_back(N%2);
        N/=2;
    }
    bool valid=true;
    memset(tmp,0,sizeof(tmp));
    for (int base=2;base<=10;base++)
    {
        LL M=0;
        int L=c.size();
        for (int i=L-1;i>=0;i--)
        {
            M=M*(LL)base+(LL)c[i];
        }
        for (LL x=2;x*x<=M;x++)
        {
            if (M%x==0)
            {
                tmp[base-2]=x; break;
            }
        }
        if (tmp[base-2]==0) {valid=false; break;}
    }
    if (valid)
    {
       Record r;
       r.num=value;
       for (int i=0;i<9;i++)
       {
           r.d[i]=tmp[i];
       }
       v.push_back(r);
    }
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C_output_small.txt","w",stdout);
    int T,N,J;
    scanf("%d",&T);
    for (int index=1;index<=T;index++)
    {
        scanf("%d%d",&N,&J);
        LL S=(LL)(1<<(N-1))+1;
        LL T=(LL)(1<<N)-1;
        v.clear();
        for (LL i=S;i<=T;i+=2)
        {
            eval(i);
            if (v.size()==J) break;
        }
        //printf("%d\n",v.size());
        printf("Case #%d:\n",index);
        for (int i=0;i<v.size();i++)
        {
            //print binary
            LL M=v[i].num;
            //printf("M=%I64d\n",M);
            for (int j=N-1;j>=0;j--)
            {
                LL mask=(LL)(1<<j);
                if ((M&mask)>0) printf("1");
                else printf("0");
            }
            for (int j=0;j<9;j++)
            {
                printf(" %I64d",v[i].d[j]);
            }
            printf("\n");
        }
    }
    return 0;
}
