#include <iostream>
#include <stdio.h>
using namespace std;
int n;
const int N = 30;
char mat[N][N];
int m[N][N];
int oristate;
int getdigit(int i)
{
    int ret=0;
    while(i)
    {
        ret+=i%2;
        i/=2;
    }
    return ret;
}
bool dfs(int wstate,int mstate)
{
    if(wstate == (1<<n)-1)
    {
        return true;
    }

    for(int i=0;i<n;i++)
    {
        if((wstate & (1<<i))!=0)continue;
        bool flag=false;

        for(int j=0;j<n;j++)
        {
            if(m[i][j]&&((mstate&(1<<j))==0))
            {
                flag=true;
                if(!dfs(wstate|(1<<i),mstate|(1<<j)))
                {
                    return false;
                }
            }
        }
        if(flag==false)
        {
            return false;
        }
    }
    return true;
}
bool check(int state)
{
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            if((state&(1<<(i*n+j)))!=0)
            {
                m[i][j]=1;
            }
            else
            {
                m[i][j]=0;
            }
        }
    }

//    for(int i=0;i<n;i++)
//        {
//            for(int j=0;j<n;j++)
//            {
//                cout<<m[i][j];
//            }
//            cout<<endl;
//        }

    if(dfs(0,0))
    {
//        cout<<"TRUE"<<endl;
        return true;
    }
//    cout<<"FALSE"<<endl;
    return false;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;
    for(int ti=1;ti<=t;ti++)
    {
        cout<<"Case #"<<ti<<": ";

        cin>>n;
        oristate = 0;
        for(int i=0;i<n;i++)
        {
            cin>>mat[i];

            for(int j=0;j<n;j++)
            {
                if(mat[i][j]=='1')
                {
                    oristate+=(1<<(i*n+j));
                }
            }
        }

        int ans = n*n+1;
        for(int i=0;i<(1<<(n*n));i++)
        {
            if((i&oristate)==oristate)
            {
                if(check(i))
                {
                    ans = min(ans,getdigit(i)-getdigit(oristate));
                }
            }
        }

        cout<<ans<<endl;
    }
    return 0;
}
