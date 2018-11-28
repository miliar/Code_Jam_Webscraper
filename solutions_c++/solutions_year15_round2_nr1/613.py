#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int t,g;
long long l,c,cl,mc,st,ta,v,gg,tt;
char n[20],cr[20],d[20];

int cti(char x)
{
    return (int)x-'0';
}
long long sti()
{
    long long x=0;
    for(int i=0;i<cl;i++)
    {
        x*=10;
        x+=cti(cr[i]);
    }
    return x;
}
void change()
{
    c+=(st-sti());
//    printf("ech %lld -> %lld\n",st-sti(),c);
    cl++;
    cr[0]='1';
    for(int i=1;i<cl;i++)   cr[i]='0';
    st*=10;
}
void flip()
{
    int id=0;
    for(int i=cl-1;i>=0;i--)    d[id++]=cr[i];
    for(int i=0;i<cl;i++)       cr[i]=d[i];
    c++;
}
long long vflip()
{
    long long x=0;
    int id=0;
    for(int i=cl-1;i>=0;i--)    d[id++]=cr[i];
    for(int i=0;i<cl;i++)
    {
        x*=10;
        x+=cti(d[i]);
    }
    return x;
}
bool pt(long long k)
{
    long long x=1;
    for(int i=0;i<l;i++)
    {
        if(k==x)    return true;
        x*=10;
    }
    return false;
}

int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A_large.txt","w",stdout);
    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        scanf("%s",n);
        l=strlen(n);
        gg=1;
        v=0;
        for(int i=0;i<l;i++)
        {
            v*=10;
            v+=cti(n[i]);
        }
        if(l==1)
        {
            printf("Case #%d: %c\n",z,n[0]);
            continue;
        }
        cr[0]='9';
        cl=1;
        st=10;
        c=9;
        while(cl<l)
        {
            change();
            if(cl==l)   break;
            g=cl/2;
            ta=9;
            for(int i=1;i<g;i++)
            {
                ta*=10;
                ta+=9;
            }
            c+=ta;
            for(int i=0,j=cl-1;i!=g;i++,j--)    cr[j]='9';
            flip();
        }
        mc=c+(v-sti());
        gg=1;
        for(int i=l-1,j=0;i>0;i--,j++)
        {
            c+=(cti(n[j])*gg);
            gg*=10;
            cr[i]=n[j];
            if(vflip()>v)   continue;
            mc=min(mc,c+1+(v-vflip()));
        }
        if(n[l-1]=='0'&&!pt(v))
        {
            v--;
            tt=v;
            for(int i=l-1;i>=0;i--)
            {
                n[i]=(char)((int)'0'+(tt%10));
                tt/=10;
            }
            c=0;
            cr[0]='9';
            cl=1;
            st=10;
            c=9;
            while(cl<l)
            {
                change();
                if(cl==l)   break;
                g=cl/2;
                ta=9;
                for(int i=1;i<g;i++)
                {
                    ta*=10;
                    ta+=9;
                }
                c+=ta;
                for(int i=0,j=cl-1;i!=g;i++,j--)    cr[j]='9';
                flip();
            }
            mc=min(mc,1+c+(v-sti()));
            gg=1;
            for(int i=l-1,j=0;i>0;i--,j++)
            {
                c+=(cti(n[j])*gg);
                gg*=10;
                cr[i]=n[j];
                if(vflip()>v)   continue;
                mc=min(mc,c+2+(v-vflip()));
            }
        }
        printf("Case #%d: %I64d\n",z,mc);
        c=0;
        mc=0;
    }
    return 0;
}
