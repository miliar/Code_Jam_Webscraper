#include <iostream>
#include <cstdio>
using namespace std;

int lawn[105][105],M,N;
bool judge1(int i,int j)
{
    for(int k=1;k<=N;k++)
    {
        if(lawn[i][j]<lawn[k][j]) return false;
    }
    return true;
}
bool judge2(int i,int j)
{
    for(int k=1;k<=M;k++)
    {
        if(lawn[i][j]<lawn[i][k]) return false;
    }
    return true;
}
bool judge()
{
    for(int i=1;i<=N;i++)
    {
        for(int j=1;j<=M;j++)
        {
            if(!judge1(i,j)&&!judge2(i,j)) return false;
        }
    }
    return true;
}
int main()
{
    int T,cas=0;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;
    while(T--)
    {
        cas++;
        cin>>N>>M;
        for(int i=1;i<=N;i++)
        {
            for(int j=1;j<=M;j++)
            {
                cin>>lawn[i][j];
                //cout<<lawn[i][j];
            }
            //cout<<endl;
        }
        if(judge()) cout<<"Case #"<<cas<<": YES"<<endl;
        else cout<<"Case #"<<cas<<": NO"<<endl;


    }
    return 0;
}
