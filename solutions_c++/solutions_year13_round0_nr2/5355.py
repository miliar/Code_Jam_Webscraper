#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<iostream>
using namespace std;
int a[105][105],mr[105],mc[105],T,N,M;
int main()
{
    freopen("test.txt","r",stdin);
    freopen("test_out.txt","w",stdout);
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>N>>M;
        memset(mr,0,sizeof(mr));
        memset(mc,0,sizeof(mc));
        for(int i=0;i<N;i++)
            for(int j=0;j<M;j++)
            {
                scanf("%d",&a[i][j]);
                mr[i]=max(mr[i],a[i][j]);
            }
        for(int i=0;i<M;i++)
            for(int j=0;j<N;j++)
                mc[i]=max(mc[i],a[j][i]);
        int ans=1;
        for(int i=0;i<N;i++)
            for(int j=0;j<M;j++)
            {
                int h=a[i][j];
                if(h<mr[i]&&h<mc[j])
                    ans=0;

            }
        printf("Case #%d: ",t);
        if(ans) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
