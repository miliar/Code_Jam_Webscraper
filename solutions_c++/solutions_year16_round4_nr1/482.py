#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stack>
#include <bitset>
#define INF 0x3f3f3f3f
#define eps 1e-8
#define FI first
#define SE second
using namespace std;
typedef long long ll;

int p[3];
int now[3];
int ans[20][10000];
int pw[20];
string fin;
string temp;
char s[10000];
char c[3]={'R','P','S'};
bool cmp(int L,int R)
{
    int mid=(L+R)/2;
    for(int i=L;i<=mid;i++)
    {
        int j=mid+i-L+1;
        if(s[i]<s[j]) return 0;
        else if(s[i]>s[j]) return 1;
    }
    return 0;
}

void swp(int L1,int R1,int L2,int R2)
{
    int j=L2;
    for(int i=L1;i<=R1;i++)
    {
        swap(s[i],s[j]);
        j++;
    }
}
bool solve(int L,int R,int id)
{
    if(L==R)
    {
        s[L]=c[id];
        return now[0]>=0&&now[1]>=0&&now[2]>=0;
    }
    int mid=(L+R)/2;
    bool sign1=0;
    bool sign2=0;
    if(id==0)
    {
        now[2]--;
        sign1=solve(L,mid,0);
        sign2=solve(mid+1,R,2);
    }
    if(id==1)
    {
        now[0]--;
        sign1=solve(L,mid,1);
        sign2=solve(mid+1,R,0);
    }
    if(id==2)
    {
        now[1]--;
        sign1=solve(L,mid,2);
        sign2=solve(mid+1,R,1);
    }
    if(sign1==0||sign2==0) return 0;
    if(cmp(L,R))   swp(L,mid,mid+1,R);
    return 1;

}
int main()
{
    freopen("A-large (2).in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    pw[0]=1;
    for(int i=1;i<=15;i++) pw[i]=pw[i-1]*2;
    for(int cas=1;cas<=t;cas++)
    {
        int n;
        bool flag=0;
        scanf("%d%d%d%d",&n,&p[0],&p[1],&p[2]);
        fin.clear();
        for(int i=0;i<3;i++)
        {
            now[0]=p[0];now[1]=p[1];now[2]=p[2];
            now[i]--;
            bool sign=solve(1,pw[n],i);
            if(sign==0) continue;
            flag=1;
            s[pw[n]+1]='\0';
            if(fin.size()==0) fin=(string)(s+1);
            else fin=min(fin,(string)s);
        }
        if(flag==0) printf("Case #%d: IMPOSSIBLE\n",cas);
        else
        {
            printf("Case #%d: ",cas);
            cout<<fin<<endl;
        }
    }
}
