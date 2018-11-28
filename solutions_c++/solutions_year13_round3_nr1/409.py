#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int n;
char str[1100000];
bool judge(char ch)
{
    if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u') return false;
    else return true;
}
long long solve(int n)
{
    int begin=0;
    int cnt=0;
    long long ans=0;
    int len=strlen(str);
    for(int i=0;i<len;i++)
    {
        if(judge(str[i])) cnt++;
        else cnt=0;

        if(cnt==n)
        {
            long long cnt1=1;
            long long cnt2=1;
            if(i-n>=begin) cnt1+=i-n+1-begin;
            if(i+1<len) cnt2+=len-1-i;
            ans+=cnt1*cnt2;

            begin=i-n+2;
            cnt--;
         //   cout<<i<<" "<<ans<<" "<<begin<<endl;
        }
    }
    return ans;
}
int main()
{
    freopen("D:\\A-large.in","r",stdin);
    freopen("D:\\out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;t--;cas++)
    {
        scanf("%s %d",str,&n);
        long long ans=solve(n);
        printf("Case #%d: %lld\n",cas,ans);
    }
}
