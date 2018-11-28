#include <iostream>
#include <cstdio>
#include <iomanip>
#include <cstring>
#include <string>
#include <queue>
#include <list>
#include <map>
using namespace std;
typedef long long ll;
typedef long double ld;
int r,c,m;
const int dx[]={1,1,0,-1,-1,-1,0,1};
const int dy[]={0,1,1,1,0,-1,-1,-1};
inline bool count(bool a[50][50],int i,int j)
{
    if (a[i][j])
        return true;
    for(int q=0;q<8;++q)
        if (i+dx[q]>=0 && i+dx[q]<r && j+dy[q]>=0 && j+dy[q]<c && a[i+dx[q]][j+dy[q]])
            return true;
    return false;
}
void dfs(bool cur[50][50],bool a[50][50],bool used[50][50],int i,int j)
{
    used[i][j]=true;
    if (cur[i][j])
        return;
    for(int q=0;q<8;++q)
        if (i+dx[q]>=0 && i+dx[q]<r && j+dy[q]>=0 && j+dy[q]<c && !a[i+dx[q]][j+dy[q]] && !used[i+dx[q]][j+dy[q]])
            dfs(cur,a,used,i+dx[q],j+dy[q]);
}
bool check(bool a[50][50])
{
    static bool used[50][50];
    static bool cur[50][50];
    for(int i=0;i<r;++i)
        for(int j=0;j<c;++j)
        {
            cur[i][j]=count(a,i,j);
            used[i][j]=false;
        }
    bool f=false;
    for(int i=0;i<r && !f;++i)
        for(int j=0;j<c && !f;++j)
            if (!cur[i][j])
            {
                f=true;
                dfs(cur,a,used,i,j);
            }
    for(int i=0;i<r;++i)
        for(int j=0;j<c;++j)
            if (!a[i][j] && !used[i][j])
                return false;
    return true;
}
bool calc(bool a[50][50],int i,int j,int cnt=0)
{
    if (i==r && !j)
    {
        if (cnt!=m)
            return false;
        return check(a);
    }
    if (cnt>m)
        return false;
    int left=(r-i-1)*c+c-j;
    if (left+cnt<m)
        return false;
    a[i][j]=1;
    int ni=i,nj=j+1;
    if (nj==c)
    {
        nj=0;
        ++ni;
    }
    if (calc(a,ni,nj,cnt+1))
        return true;
    a[i][j]=0;
    if (calc(a,ni,nj,cnt))
        return true;
    return false;
}
void print(bool a[50][50])
{
    bool f=true;
    for(int i=0;i<r;++i,cout<<"\n")
        for(int j=0;j<c;++j)
            if (!a[i][j])
            {
                bool res=count(a,i,j);
                if (f && !res)
                    cout<<'c';
                else
                    cout<<'.';
                if (!res)
                    f=false;
            } else
                cout<<'*';
}
int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    bool a[50][50];
    for(int q=0;q<t;++q)
    {
        cin>>r>>c>>m;
        cout<<"Case #"<<q+1<<":\n";
        if (m==r*c-1)
        {
            for(int i=0;i<r;++i,cout<<"\n")
                for(int j=0;j<c;++j)
                    if (!i && !j)
                        cout<<'c';
                    else
                        cout<<'*';
            continue;
        }
        if (calc(a,0,0))
            print(a);
        else
            cout<<"Impossible\n";
    }
    return 0;
}
