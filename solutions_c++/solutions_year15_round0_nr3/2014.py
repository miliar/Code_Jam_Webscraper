#include <stdio.h>
#include <map>

using namespace std;

char mat[4][4]={{'1','i','j','k'},{'i','1','k','j'},{'j','k','1','i'},{'k','j','i','1'}};
int signmat[4][4]={{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};

map <char,int> M;

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("smallc.in","r",stdin);
        freopen("outsmallc.txt","w",stdout);
    #endif
    M['1']=0;
    M['i']=1;
    M['j']=2;
    M['k']=3;
    int t;
    scanf ("%d",&t);
    int j;
    for (j=1;j<=t;++j)
    {
        int l,x;
        char A[100000];
        int pos;
        scanf ("%d %d",&l,&x);
        scanf ("%s",A);
        x--;
        int i;
        pos=l;
        while (x>0)
        {
            for (i=0;i<l;++i)
                A[pos++]=A[i];
            x--;
        }
        A[pos]='\0';
        char res[100000];
        int sign[100000];
        int ans=1;
        res[0]=A[0];
        sign[0]=1;
        for (i=1;i<pos;++i)
        {
            res[i]=mat[M[res[i-1]]][M[A[i]]];
            sign[i]=sign[i-1]*signmat[M[res[i-1]]][M[A[i]]];
        }
        for (i=0;i<pos;++i)
            if (res[i]=='i'&&sign[i]==1)
                break;
        if (i==pos)
            ans=0;
        i++;
        for (i;i<pos;++i)
        {
            if (res[i]=='k'&&sign[i]==1)
                break;
        }
        if (i==pos)
            ans=0;
        if (res[pos-1]!='1'||sign[pos-1]!=-1)
            ans=0;
        if (ans==0)
            printf("Case #%d: NO\n",j);
        else
            printf("Case #%d: YES\n",j);
    }
    return 0;
}
