/*Code jam 15 q3*/
#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<fstream>
#define I 2
#define J 3
#define K 4
#define CONSTANT 103
using namespace std;
int mul(int,int);
int table[4][4];
int main()
{
    int i=0,j=0,k=0,l,noc,nor,t,loop;
    char c[10000];
    int fl[10000];
    char *p1,*p2,*p3;
    table[1][1]=1;table[1][2]=2;table[1][3]=3;table[1][4]=4;
    table[2][1]=2,table[2][2]=-1,table[2][3]=4,table[2][4]=-3;
    table[3][1]=3,table[3][2]=-4,table[3][3]=-1,table[3][4]=2;
    table[4][1]=4,table[4][2]=3,table[4][3]=-2,table[4][4]=-1;
    int length;
    FILE *out;
    FILE *in;
    in=freopen("in.in","r",stdin);
    out=freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(loop=0;loop<t;loop++)
    {
        k=0;
        scanf("%d%d",&noc,&nor);

        scanf("%s",c);

        for(i=0;i<nor;i++)
        {
            for(j=0;j<noc;j++)
            {
                fl[k++]=c[j]-CONSTANT;
            }
        }
        length=noc*nor;
        int res=1;
        i=0;
        while(res!=I&&i<=length-3)
        {
            res=mul(res,fl[i++]);
        }
        if(res!=I)
        {
            printf("Case #%d: NO\n",loop+1);
            continue;
        }
        res=1;
        j=length-1;
        while(res!=K&&j>i)
        {
            res=mul(fl[j--],res);
        }
        if(res!=K)
        {
            printf("Case #%d: NO\n",loop+1);
            continue;
        }
        res=1;
        for(k=i;k<=j;k++)
        {
            res=mul(res,fl[k]);
        }
        if(res!=J)
        {
            printf("Case #%d: NO\n",loop+1);
            continue;
        }
        else
        {
            printf("Case #%d: YES\n",loop+1);
        }
    }
    return 0;
}
/*int findchar(int *fl,int start,int last,int toFind)
{
    bool flag=false;
    int res;
    int next,i;
    if(fl[start]==toFind)
        return start;
    res=fl[start];
    for(i=start;i<last;i++)
    {
        next=i+1;
        res=mul(res,fl[next]);
        if(res==toFind)
        {
            flag=true;
            break;
        }
    }
    if(flag)
        return next;
    return -1;
}
int findahead(int *fl,int start,int last,int toFind)
{
    bool flag=false;
    int res;
    int next,i;
    res=toFind;
    for(i=start;i<=last;i++)
    {
        res=mul(res,fl[i]);
        if(res==toFind)
        {
            flag=true;
            break;
        }
    }
    if(flag)
        return i;
    return -1;
}*/
int mul(int x,int y)
{
    int s1=1,s2=1;
    if(x<0){
        s1=-1;
        x=x*-1;
    }
    if(y<0){
        s2=-1;
        y=y*-1;
    }
    return table[x][y]*s1*s2;
}
