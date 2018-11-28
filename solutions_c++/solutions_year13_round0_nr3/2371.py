#include<cstdio>
#include<iostream>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;
typedef pair<int,int> PII;
#define PB push_back
#define MP make_pair
#define fi first
#define se second
VS v;
string add(string a, string b)
{
    if(a.size()<b.size())
        return add(b,a);
    while(b.size()<a.size())
        b = "0"+b;
    for(int i = 0;i<a.size();i++)
    {
        a[i] += b[i] - '0';
    }
    return a;
}
string mul(string a,int n)
{
    for(int i=0;i<a.size();i++)
        a[i] = (a[i] - '0')*n + '0';
    return a;
}
string sqr(string a)
{
    string ret = "";
    int m = 0;
    string b = a;
    //cout<<a<<endl;
    for(int i=0;i<a.size();i++)
    {
        m = a[i] - '0';
        //cout<<b<<" "<<m<<endl;
        ret = add(ret, mul(b,m));
        b = b + "0";
    }
    return ret;
}
void dfs(string now, int sum)
{
    int i;
    if(now.size()>26)
        return;
    for(i=0;i<3;i++)
    {
        int ns = 2*i*i+sum;
        if(ns<10)
        {
            char c = i+'0';
            string next = c+now+c;
            //cout<<next<<endl;
            if(c!='0'&&next.size()<=50)
                v.PB(sqr(next));
            dfs(next,ns);
        }
    }
}
bool cmp(string a, string b)
{
    if(a.size()==b.size())
    {
        return a<b;
    }
    return a.size()<b.size();
}
int main()
{
    int t;
    string a,b;
    int i,j;
    freopen("cl1.in","r",stdin);
    freopen("cl1.out","w",stdout);
    v.clear();
    v.PB("1");
    v.PB("4");
    v.PB("9");
    dfs("0",0);
    dfs("1",1);
    dfs("2",4);
    dfs("",0);
    sort(v.begin(),v.end(),cmp);
    //for(i=0;i<v.size();i++)
        //cout<<v[i]<<endl;
    //printf("%d\n",v.size());
    scanf("%d",&t);
    for(int cnt = 1;cnt<=t;cnt++)
    {
        //scanf("%d %d",&a,&b);
        cin>>a;cin>>b;
        //cout<<a<<" "<<b<<endl;
        int ret = 0;
        for(i=0;i<v.size();i++)
        {
            if((v[i] == a)||cmp(a,v[i]))
                if((v[i] == b)||cmp(v[i],b))
                {
                    //printf("%d\n",i);
                    ret++;
                }

        }
        printf("Case #%d: %d\n",cnt,ret);
    }
    return 0;
}
