#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;
#define DEBUG

int m[110][110];
int sm[110][110];
pair<int,int> fir[110];
int ans[110][110];
int out[110];
bool fillCol[110];

bool dfs(int now,int col,int n)
{
    if(col==n)
    {
        //每行寻找是否存在，可错误一次

        bool notFind = false;
        int nowRow = 1;


        for(int i=0;i<2*n-1;i++)
        {
            //每行输入
            if(fillCol[i])continue;//已经填入

            if(ans[nowRow][0]!=sm[i][0])
            {
                for(int j=0;j<n;j++)
                {
                    out[j]=ans[nowRow][j];
                }
                nowRow++;
            }
            if(nowRow>=n)return false;
            for(int j=0;j<n;j++)
            {
                if(ans[nowRow][j]!=sm[i][j])return false;
            }
            nowRow++;
        }
        if(nowRow!=n)
        {
            for(int i=0;i<n;i++)
            {
                out[i]=ans[nowRow][i];
            }
        }
        return true;
    }
    if(now>=2*n)return false;

    if(sm[now][0]>ans[0][col])
    {
        return false;
    }

    if(sm[now][0]==ans[0][col])
    {

        for(int i=0;i<n;i++)
        {
            ans[i][col]=sm[now][i];
        }
        fillCol[now]=true;
        if(dfs(now+1,col+1,n))
        {
            return true;
        }
        fillCol[now]=false;
    }


    if(dfs(now+1,col,n))
    {
        return true;
    }
    return false;
}
bool dfs1(int now,int col,int n)
{
    if(col==n)
    {
        //每行寻找是否存在，可错误一次

        bool notFind = false;
        int nowRow = 1;



        for(int i=0;i<2*n-1;i++)
        {
            //每行输入
            if(fillCol[i])continue;//已经填入
            for(int j=1;j<n;j++)
            {
                if(ans[nowRow][j]!=sm[i][j])return false;
            }
            ans[nowRow][0]=sm[i][0];
            nowRow++;
        }
        return true;
    }
    if(now>=2*n)return false;

    if(sm[now][0]>ans[0][col])
    {
        return false;
    }

    if(sm[now][0]==ans[0][col])
    {

        for(int i=0;i<n;i++)
        {
            ans[i][col]=sm[now][i];
        }
        fillCol[now]=true;
        if(dfs1(now+1,col+1,n))
        {
            return true;
        }
        fillCol[now]=false;
    }


    if(dfs1(now+1,col,n))
    {
        return true;
    }
    return false;
}

bool cmp(vector<int> a, vector<int> b)
{
    return a[0]<b[0];
}
int main()
{
    #ifdef DEBUG
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif // DEBUG

    int t;
    cin>>t;

    for(int ti=1;ti<=t;ti++)
    {
        int n;
        cin>>n;

        int minNum = 3000;
        int minIndex = -1;
        for(int i=0;i<2*n-1;i++)
        {

            for(int j=0;j<n;j++)
            {
                cin>>m[i][j];
            }
            fir[i].first = m[i][0];
            fir[i].second = i;
        }

        sort(fir,fir+2*n-1);
        memset(fillCol,false,sizeof(fillCol));

        for(int i=0;i<2*n-1;i++)
        {
            for(int j=0;j<n;j++)
            {
                sm[i][j]=m[fir[i].second][j];
                //cout<<sm[i][j]<<' ';
            }
            //cout<<endl;
        }
        //cout<<endl;

        cout<<"Case #"<<ti<<":";
        if(sm[0][0]==sm[1][0])
        {

        for(int i=0;i<n;i++)
        {
            ans[0][i]=sm[0][i];
            ans[i][0]=sm[1][i];
        }
        fillCol[0]=true;
        fillCol[1]=true;

        if(dfs(2,1,n))
        {
            //成功
            for(int i=0;i<n;i++)
            {
                cout<<' '<<out[i];
            }
            cout<<endl;
        }
        else
        {
            //再测试
            memset(fillCol, false,sizeof(fillCol));
            for(int i=0;i<n;i++)
            {
                ans[0][i]=sm[1][i];
                ans[i][0]=sm[0][i];
            }
            fillCol[0]=true;
            fillCol[1]=true;
            dfs(2,1,n);

            for(int i=0;i<n;i++)
            {
                cout<<' '<<out[i];
            }
            cout<<endl;
        }
        }
        else
        {
            for(int i=0;i<n;i++)
            {
                ans[0][i]=sm[0][i];
            }
            fillCol[0]=true;
            dfs1(1,1,n);

            for(int i=0;i<n;i++)
            {
                cout<<' '<<ans[i][0];
            }
            cout<<endl;
        }
    }
    return 0;
}
