#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char a[102];
int b[102];
int l;
int fun(int i,int r)
{
    if(i==0)
    {
        if(a[i]=='+'&&r>0||(a[i]=='-'&&r<0)) return 0;
        return 1;
    }
    if(a[i]=='+'&&r>0||(a[i]=='-'&&r<0)) return fun(i-1,r);
    else return fun(i-1,-r)+1;
}
int main()
{
    int n,m,sum;
    int i,j,t,kk;
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    scanf("%d\n",&t);
    kk=t;
    while(t--)
    {
        gets(a);
        l=strlen(a)-1;
        sum=fun(l,1);
        printf("Case #%d: %d\n",kk-t,sum);
    }
    return 0;
}
/*
50
-
-+
+-
+++
--+-
----
++++
-+-+
+-+-
*/
