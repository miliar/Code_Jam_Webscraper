#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<map>
#include<queue>
#include<string>
#include<vector>
#include<ctime>
#include<stack>
#include<sstream>
using namespace std;
vector<long long> v;
bool ok(long long a)
{
    char s[105];
    int len;
    memset(s,0,sizeof(s));
    sprintf(s,"%lld",a);
    len=strlen(s);
    for(int i=0;i<len/2;i++)
        if(s[i]!=s[len-1-i])
            return 0;
    return 1;
}
int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("C-large-1.out","w",stdout);
    v.clear();
    long long i;
    for(i=0;i<=10000000;i++)
        if(ok(i) && ok(i*i))
            v.push_back(i*i);
    int t,tt=0,cnt;
    long long a,b;
    scanf("%d",&t);
    while(t--)
    {
        tt++;
        cnt=0;
        scanf("%lld%lld",&a,&b);
        for(i=0;i<v.size();i++)
            if(v[i]>=a && v[i]<=b)
                cnt++;
        printf("Case #%d: %d\n",tt,cnt);
    }
    return 0;
}
