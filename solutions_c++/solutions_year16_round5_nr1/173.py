#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
char s[20005],stk[20005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        int top=0,res=0;
        scanf("%s",s);
        for(int i=0;s[i];i++)
        {
            if(s[i]=='C')
            {
                if(top && stk[top-1]=='C')top--,res+=10;
                else stk[top++]='C';
            }
            else
            {
                if(top && stk[top-1]=='J')top--,res+=10;
                else stk[top++]='J';
            }
            //printf("%d\n",top);
        }
        res+=5*(top/2);
        printf("Case #%d: %d\n",ca,res);
    }
    return 0;
}
