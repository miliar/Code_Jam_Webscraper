#include<cstdio>
typedef long long ll;
const int maxn=1e4+10;
const char table[][5]={ "1ijk",
                        "i1kj",
                        "jk1i",
                        "kji1"};
const int signs[][4]={  {0,0,0,0},
                        {0,1,0,1},
                        {0,1,1,0},
                        {0,0,1,1}};
int T,n,cas=1;
ll m;
char s[maxn];
int mul(char &c,char a,char b)
{
    int x=(a=='1'?0:a-'h');
    int y=(b=='1'?0:b-'h');
    c=table[x][y];
    return signs[x][y];
}
int div(char &b,char a,char c)
{
    char ch;
    for (int i=0;i<4;i++)
    {
        int s=mul(ch,a,"1ijk"[i]);
        if(ch==c)
        {
            b="1ijk"[i];
            return s;
        }
    }
    return -1;
}
struct ty
{
    char ch;
    int sign;
}pre[maxn];
ty operator *(const ty &a,const ty &b)
{
    ty c;
    c.sign=a.sign^b.sign^mul(c.ch,a.ch,b.ch);

    //printf("%c%c * %c%c =%c%c\n"," -"[a.sign],a.ch," -"[b.sign],b.ch," -"[c.sign],c.ch);

    return c;
}
ty operator /(const ty &c,const ty &a)
{
    ty b;
    b.sign=a.sign^c.sign^div(b.ch,a.ch,c.ch);
    return b;
}
ty pow(ty x,ll n)
{
    ty ret=(ty){'1',0};
    while (n>0)
    {
        if (n&1) ret=ret*x;
        n>>=1;
        x=x*x;
    }
    return ret;
}
ll findi()
{
    ll ret=-1;
    for (int i=1;i<=n;i++)
    {
        for (int j=0;j<=10;j++)
        {
            ty tmp=pow(pre[n],j)*pre[i];
            //printf("i=%d j=%d pos=%I64d tmp=%c%c\n",i,j,j*n+i-1," -"[tmp.sign],tmp.ch);
            ll pos=j*n+i-1;
            if ((tmp.ch=='i'&&tmp.sign==0)&&(ret==-1||ret>pos)) ret=pos;
        }
    }
    return ret;
}
ll findk()
{
    ll ret=-1;
    for (int i=1;i<=n;i++)
    {
        for (int j=0;j<=10;j++)
        {
            ty tmp=pre[n]/pre[i-1]*pow(pre[n],j);
            ll pos=n*m-(j*n+n-i+1);
            if ((tmp.ch=='k'&&tmp.sign==0)&&(ret<pos)) ret=pos;
        }
    }
    return ret;
}
bool solve()
{
    pre[0]=(ty){'1',0};
    for (int i=1;i<=n;i++) pre[i]=pre[i-1]*(ty){s[i-1],0};
    ty ret=pow(pre[n],m);
    //printf("pre[n]=%c %d\n",pre[n].ch,pre[n].sign);
    //printf("ret=%c %d\n",ret.ch,ret.sign);

    if (ret.ch!='1'||ret.sign!=1) return 0;
    ll posi=findi();
    //printf("%I64d\n",posi);
    ll posk=findk();
    //printf("%I64d\n",posk);
    if (-1<posi&&posi<posk&&posk<n*m) return 1;
    return 0;
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d%I64d%s",&n,&m,s);printf("Case #%d: ",cas++);
        if (solve()) puts("YES");
        else puts("NO");
    }
    return 0;
}
