#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
char mat[60][60];
struct node
{
    int a,b,c;
    node(){a=-1;}
    node(int x,int y,int z)
    {
        a=x;b=y;c=z;
    }
};
node dp[60][60][2520];
int n,m,l;
bool markc;
bool dfs(int p,int h,int s)
{
//    cout<<p<<endl;
    if(dp[p][h][s].a==-1)return false;
    if(p==0)return true;
//    cout<<p<<' '<<h<<' '<<s<<' '<<dp[p][h][s]<<endl;
//    if(h<0||s<0||!dp[p][h][s])return false;
//    if(p==0)return true;
//
//    bool flag=false;
//
//    if(!flag)
//        flag=dfs(p-1,0,s-h);
//
//    if(!flag)
//    {
//        flag=dfs(p-1,h-1,s-h);
//    }
//
//    if(!flag)
//    {
//        flag=dfs(p-1,h,s-h);
//    }
    bool flag=true;
    node nod=dp[p][h][s];
    dfs(nod.a,nod.b,nod.c);

    if(flag)
    {
        for(int i=0;i<h;i++)mat[p-1][i]='.';
        for(int i=h;i<m;i++)mat[p-1][i]='*';
    }
    return flag;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;

    for(int ti=0; ti<t; ti++)
    {
        cout<<"Case #"<<ti+1<<":"<<endl;
        markc=false;

        cin>>n>>m>>l;

        int sum=n*m-l;
        for(int i=0;i<=n;i++)
        {
            for(int j=0;j<=m;j++)
            {
                for(int k=0;k<=sum;k++)
                {
                    dp[i][j][k]=node();
                }
            }
        }
        dp[0][0][0]=node(0,0,0);
        for(int p=0;p<n;p++)
        {
            for(int h=0;h<=m;h++)
            {
                for(int s=0;s<=sum;s++)
                {
                    if(dp[p][h][s].a!=-1)
                    {
                        struct node nod=node(p,h,s);
                        if(h==0)
                        {
                            if(p!=n-1||n==1)
                            {
                                dp[p+1][0][s]=nod;
                                if(m==1)dp[p+1][1][s+1]=nod;
                                for(int h2=2;h2<=m&&s+h2<=sum;h2++)
                                {

                                    dp[p+1][h2][s+h2]=nod;
                                }
                            }
                            if(sum==1&&p==n-1)dp[p+1][1][1]=nod;
                        }
                        else if(h==1)
                        {
                            if(m==1&&s+1<=sum)
                            {
                                dp[p+1][1][s+1]=nod;
                            }
                        }
                        else
                        {
                            if(s+h<=sum)dp[p+1][h][s+h]=nod;
                            if(p+1<n)
                            {
                                for(int k=h+1;k<=m&&s+h<=sum;k++)
                                {
                                    dp[p+1][k][s+k]=nod;
                                }
                            }
                        }

                    }
                }
            }
        }
//        cout<<"dfssdfsd"<<endl;
        bool flag=false;
//        cout<<m<<endl;
        for(int h=m;h>0&&!flag;h--)
        {
//            cout<<"D"<<n<<' '<<h<<' '<<sum<<endl;
            flag=dfs(n,h,sum);
//            if(flag)cout<<n<<' '<<h<<' '<<sum<<endl;
        }
        mat[n-1][0]='c';
        if(!flag)
        {
//            cout<<n<<' '<<m<<' '<<l<<endl;
            cout<<"Impossible"<<endl;
        }
        else
        {
//            cout<<n<<endl;
            int cnt=0;
            for(int i=0;i<n;i++)
            {
                mat[i][m]='\0';

//                cout<<strlen(mat[i])<<' '<<m;
//                for(int j=0;j<m;j++)
//                {
//                    if(mat[i][j]=='*')cnt++;
//                }
                cout<<mat[i]<<endl;
            }
//            while(cnt!=l);
        }
    }
    return 0;
}
