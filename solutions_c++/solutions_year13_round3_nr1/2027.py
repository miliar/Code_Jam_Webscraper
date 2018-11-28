#include<iostream>
#include<stdio.h>
#include<cstring>
#include<iomanip>
#include<cmath>
using namespace std;
int n,L,ans,start;
char arr[1000001];
void calc1(int i)
{
    ans+=( (L-i-1) + (i-n+1-start) + ((L-i-1)*(i-n+1-start)));
}
void calc2(int i)
{
    ans+=(L-i-1);
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    //freopen("input1.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    int t,cases,i,cnt;
    bool flag;
    scanf("%d",&t);
    for(cases=1;cases<=t;cases++)
    {
        scanf("%s %d",&arr,&n);
        L=strlen(arr);
        flag=0;   cnt=0;    ans=0;   start=0;
        for(i=0;i<L;i++)
        {
            if(arr[i]=='a'||arr[i]=='i'||arr[i]=='o'||arr[i]=='u'||arr[i]=='e')
            {
                if(flag)
                {
                    start=i-n+1;
                    //L-=start;
                    flag=0;
                }
                    cnt=0; continue;
            }
            cnt++;
            if(cnt>=n)
            {
                ans++;
                //cout<<arr[i]<<endl;
                if(!flag)
                {
                    flag=1;
                    calc1(i);
                    //cout<<start<<" "<<L<<endl;
                    //cout<<ans<<endl;
                }
                else
                    calc2(i);
            }
        }
        printf("Case #%d: %d\n",cases,ans);
    }
    return 0;
}
