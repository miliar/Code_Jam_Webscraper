#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
int n,L,ans,st;
void f1(int i)
{
    ans+=( (L-i-1) + (i-n+1-st) + ((L-i-1)*(i-n+1-st)));
}
void f2(int i)
{
    ans+=(L-i-1);
}
char arr[1000001];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output1.txt","w",stdout);
    int t,cases,i,cnt;
    bool ff;
    scanf("%d",&t);
    for(cases=1;cases<=t;cases++)
    {
        scanf("%s %d",&arr,&n);
        L=strlen(arr);
        ff=0;   cnt=0;    ans=0;   st=0;
        for(i=0;i<L;i++)
        {
            if(arr[i]=='a'||arr[i]=='i'||arr[i]=='o'||arr[i]=='u'||arr[i]=='e')
            {
                if(ff)
                {
                    st=i-n+1;
                    ff=0;
                }
                    cnt=0; continue;
            }
            cnt++;
            if(cnt>=n)
            {
                ans++;
                if(!ff)
                {
                    ff=1;
                    f1(i);
                }
                else
                    f2(i);
            }
        }
        printf("Case #%d: %d\n",cases,ans);
    }
    return 0;
}
