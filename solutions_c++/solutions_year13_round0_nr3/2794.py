#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstring>
using namespace std;
bool check(int n)
{
    char num[8];
    itoa(n,num,10);
    int len=strlen(num);
    for(int i=0,j=len-1;i<j;++i,--j)
    {
        if(num[i]!=num[j])return false;
    }
    return true;
}
int main()
{
    #ifdef LOCAL_DEBUG
        freopen("E:\\C-small-attempt0.in","r",stdin);
        freopen("E:\\C-small-attempt0.out","w",stdout);
    #endif
    bool flag[2000];
    int T,L,R,cnt;
    memset(flag,0,sizeof(flag));
    for(int i=1;i<40;++i)
    {
        if(check(i)&&check(i*i))
        {
            flag[i*i]=true;
        }
    }
    cin>>T;
    for(int t=1;t<=T;++t)
    {
        cnt=0;
        for(cin>>L>>R;L<=R;++L)
        {
            if(flag[L])++cnt;
        }
        cout<<"Case #"<<t<<": "<<cnt<<'\n';
    }
}
