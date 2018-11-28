#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;

const int maxn=105;
int h[maxn][maxn],heng[maxn],shu[maxn];
int n,m;

int main()
{
    int T,cs=0;
    cin>>T;
    ofstream ff("a.out");
    while(T--){
        cs++;
        scanf("%d%d",&n,&m);
        memset(heng,0,sizeof(heng));
        memset(shu,0,sizeof(shu));
        for(int i=0;i<n;++i)
        for(int j=0;j<m;++j){
            scanf("%d",&h[i][j]);
            heng[i]=max(heng[i],h[i][j]);
            shu[j]=max(shu[j],h[i][j]);
        }
        int flag=0;
        for(int i=0;i<n&&!flag;++i)
        for(int j=0;j<m;++j){
            if(h[i][j]<heng[i]&&h[i][j]<shu[j]){
                flag=1;
                break;
            }
        }
        if(!flag) ff<<"Case #"<<cs<<": YES"<<endl;
        //printf("Case #%d: YES\n",cs);
        else ff<<"Case #"<<cs<<": NO"<<endl;
        //printf("Case #%d: NO\n",cs);
    }
    ff.close();
    return 0;
}
