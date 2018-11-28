#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstring>
using namespace std;
int main()
{
    //freopen("E:\\B-large.in","r",stdin);
    //freopen("E:\\B-large.out","w",stdout);
    bool possible[128][128],completed;
    int grass[128][128];
    int T,N,M,max;
    cin>>T;
    for(int t=1;t<=T;++t)
    {
        cin>>N>>M;
        completed=true;
        memset(possible,0,sizeof(possible));
        for(int i=0;i<N;++i)
        {
            max=-1;
            for(int j=0;j<M;++j)
            {
                scanf("%d",&grass[i][j]);
                if(max<grass[i][j])max=grass[i][j];
            }
            for(int j=0;j<M;++j)
            {
                if(max==grass[i][j])possible[i][j]=true;
            }
        }
        for(int j=0;j<M;++j)
        {
            max=-1;
            for(int i=0;i<N;++i)
            {
                if(max<grass[i][j])max=grass[i][j];
            }
            for(int i=0;i<N;++i)
            {
                if(max==grass[i][j])possible[i][j]=true;
            }
        }
        for(int i=0;i<N;++i)
        {
            for(int j=0;j<M;++j)
            {
                if(!possible[i][j])
                {
                    completed=false;
                    break;
                }
            }
        }
        cout<<"Case #"<<t<<": ";
        if(completed)
        {
            cout<<"YES\n";
        }
        else
        {
            cout<<"NO\n";
        }
    }
}
