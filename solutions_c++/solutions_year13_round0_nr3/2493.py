#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;
vector<long long> ans;
bool judge2(long long k)
{
    char str[1005];
    sprintf(str,"%lld",k);
    int len=strlen(str);
    int low=0,high=len-1;
    while(low<high)
    {
        if(str[low++]!=str[high--])
            return false;
    }
    return true;
}
int deep,num[10];
bool judge(int k)
{
    long long temp=0;
    //cout<<temp<<endl;
    for(int i=0;i<k;i++)
        temp=temp*10+num[i];
    for(int i=k-1;i>=0;i--)
        temp=temp*10+num[i];
    if(judge2(temp*temp))
        ans.push_back(temp*temp);
    //cout<<temp<<endl;
    temp=0;
    for(int i=0;i<k;i++)
        temp=temp*10+num[i];
    for(int i=k-2;i>=0;i--)
        temp=temp*10+num[i];
    if(judge2(temp*temp))
        ans.push_back(temp*temp);
    //cout<<temp<<endl;
}
void dfsid(int now)
{
    if(now==deep)
    {
        judge(now);
        return;
    }
    for(int i=(now==0?1:0);i<10;i++)
    {
        num[now]=i;
        dfsid(now+1);
    }
}
int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("out.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(deep=1;deep<=4;deep++)
        dfsid(0);
    sort(ans.begin(),ans.end());
    //cout<<ans.size()<<endl;
    //for(int i=0;i<ans.size();i++)
        //cout<<ans[i]<<endl;
    //cout<<ans.size()<<endl;
    /*int p=0;
    for(int i=1;i*i<=1e14;i++)
    {
        if(judge(i)&&judge(i*i))
            num[p++]=i*i;
    }*/
    //return 0;
    //for(int i=0;i<p;i++)
        //cout<<num[i]<<endl;
    for(int cas=1;cas<=t;cas++)
    {
        printf("Case #%d: ",cas);
        long long a,b;
        scanf("%lld%lld",&a,&b);
        printf("%d\n",upper_bound(ans.begin(),ans.end(),b)-lower_bound(ans.begin(),ans.end(),a));
    }
}
