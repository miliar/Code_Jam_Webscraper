#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin>>T;
	for (int cas=1;cas<=T;++cas)
	{
        int N,M;
        cin>>N>>M;
        int a[N][M];
        for (int i=0;i<N;++i)
            for (int j=0;j<M;++j)
                scanf("%d",&a[i][j]);
        int maxrow[101]={};
        int maxcol[101]={};
        for (int i=0;i<N;++i)
            for (int j=0;j<M;++j)
            {
                maxrow[i]=max(maxrow[i],a[i][j]);
                maxcol[j]=max(maxcol[j],a[i][j]);
                }
        string ans="YES";
        for (int i=0;i<N;++i)
            for (int j=0;j<M;++j)
                if (a[i][j]<maxrow[i]&&a[i][j]<maxcol[j])
                {
                   ans="NO";
                   }
        cout<<"Case #"<<cas<<": "<<ans<<endl;
        }
    return 0;
    }
