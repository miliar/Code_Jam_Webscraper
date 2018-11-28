#include<cstdio>
#include<string>
#include<algorithm>
#include<iostream>
int mul[5][5]=
{{0,0,0,0,0},
{0,1,2,3,4},
{0,2,-1,4,-3},
{0,3,-4,-1,2},
{0,4,3,-2,-1},
};
int x[40005];
using namespace std;
int abs(int a)
{
    if(a<0)
        return -a;
    else
        return a;
}
int init(int st,long long ro)
{
    if(st==1)
        return false;
    if(st==-1&&ro%2==1)
        return true;
    if(st!=-1&&ro%4==2)
        return true;
    return false;
}
int main()
{
    freopen("2015_Q_C_l.in","r",stdin);
    freopen("2015_Q_C_l.out","w",stdout);
    bool ch;
    int T,l,nw,r;
    string s,in;
    long long R;
    scanf("%d",&T);
    for(int I=1,i,j;I<=T;I++)
    {
        nw=1;
        s="";
        scanf("%d%lld",&l,&R);
        cin>>in;
        if(R>8)
        {
            r=(int)min((long long)4,R);
            for(i=0;i<r;i++)
                s+=in;
            for(i=0;i<r*l;i++)
            {
                switch(s[i])
                {
                     case 'i':x[i]=2;break;
                     case 'j':x[i]=3;break;
                     case 'k':x[i]=4;break;
                }
            }
            for(i=0;i<l;i++)
                nw=((nw>0)?1:-1)*mul[abs(nw)][x[i]];
            ch=init(nw,R);
            nw=1;
            for(i=0;i<r*l;i++)
            {
                nw=((nw>0)?1:-1)*mul[abs(nw)][x[i]];
                if(nw==2)
                    break;
            }
            if(i>=r*l)
                ch=false;
            nw=1;
            for(i=r*l-1;i>=0;i--)
            {
                nw=((nw>0)?1:-1)*mul[x[i]][abs(nw)];
                if(nw==4)
                    break;
            }
            if(i<0)
                ch=false;
        }
        else
        {
            ch=true;
            r=int(R);
            for(i=0;i<r;i++)
                s+=in;
            for(i=0;i<r*l;i++)
            {
                switch(s[i])
                {
                     case 'i':x[i]=2;break;
                     case 'j':x[i]=3;break;
                     case 'k':x[i]=4;break;
                }
                //printf("%d",x[i]);
            }
            //printf("\n");
            for(i=0;i<r*l;i++)
                nw=((nw>0)?1:-1)*mul[abs(nw)][x[i]];
            if(nw!=-1)
                ch=false;
            nw=1;
            for(i=0;i<l*r;i++)
            {
                nw=((nw>0)?1:-1)*mul[abs(nw)][x[i]];
                //printf("-> %d\n",nw);
                if(nw==2)
                    break;
            }
            nw=1;
            for(j=r*l-1;j>i;j--)
            {
                nw=((nw>0)?1:-1)*mul[x[j]][abs(nw)];
                //printf("%d <-\n",nw);
                if(nw==4)
                    break;
            }
            if(j<=i)
                ch=false;
            //printf("i = %d vs j = %d\n",i,j);
        }
        printf("Case #%d: ",I);
        if(ch)
            printf("YES\n");
        else
            printf("NO\n");
    }
}
