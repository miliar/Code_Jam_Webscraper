
#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;
const int maxn=1010000;
bool pri[maxn];
long long Div[maxn];
int n,m,cnt=0;
void init()
{
    memset(pri,true,sizeof(pri));
    memset(Div,-1,sizeof(Div));
    pri[1]=false;
    for(int i=2;i<maxn;i++)
    {
        if(pri[i])
        {
            Div[i]=-1;
            for(int j=2;j*i<maxn;j++)
            {
                pri[i*j]=false;
                Div[i*j]=i;
            }
        }
    }
}
long long isPri(long long x)
{
    if(x<maxn) return Div[x];
    for(int i=2;i<1000;i++)
    {
        if(x%i==0) return i;
    }
    return -1ll;
}
vector<int> ok(long long x)
{
    vector<int> vec;
    vec.clear();
    for(int i=2;i<=10;i++)
    {
        long long mul=0;
        long long h=x;
        long long tmp=1;
        while(h>0)
        {
            if(h&1) mul=mul+tmp;
            tmp*=i;
            h=h>>1;
        }
        int t=isPri(mul);
        if(t==-1)
        {
            vec.clear();
            return vec;
        }
        else
            vec.push_back(t);
    }
    return vec;
}
void dfs(int deep,long long x)
{
    //cout<<deep<<" "<<x<<endl;
    if(cnt>=m) return ;
    if(deep==n-1)
    {
        x=x*2+1;
        vector<int> p=ok(x);
        if(p.size()!=0)
        {
            cnt++;
            long long temp=x;
            string ans="";
            while(temp>0)
            {
                ans+='0'+temp%2;
                temp/=2;
            }
            reverse(ans.begin(),ans.end());
            cout<<ans<<" ";
            for(int j=0;j<p.size();j++)
                cout<<p[j]<<" ";
            cout<<endl;
        }
        return ;
    }
    for(int i=0;i<2;i++)
    {
        long long k=x*2+i;
        dfs(deep+1,k);
    }
}
int main(int argc, char *argv[]) {
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    init();
    int T;
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>n>>m;
        printf("Case #%d:\n",ca);
        dfs(1,1);
    }
	return 0;
}

