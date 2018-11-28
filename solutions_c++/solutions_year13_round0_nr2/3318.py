#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>
using namespace std;

struct po
{
    int x,y,h;
    po(int a, int b, int c):x(a),y(b),h(c){}
};

int operator<(const po& a, const po& b)
{
    return a.h<b.h;
}

int T,n,m;
int a[120][120];
int g[120][120];
int demo[120][120];
int sumrow[120];
int sumcol[120];
vector<po> vp;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>T;
    int cs=0;
    while (T--)
    {
        cs++;
        vp.clear();
        cin>>n>>m;
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
            {
                scanf("%d",&a[i][j]);
                vp.push_back(po(i,j,a[i][j]));
            }
        sort(vp.begin(),vp.end());
        memset(sumrow,0,sizeof(sumrow));
        memset(sumcol,0,sizeof(sumcol));
        memset(demo,0,sizeof(demo));
        memset(g,0,sizeof(g));
        bool ans=true;
        for (int i=0;i<vp.size();i++)
        {
            vector<int> nrs;
            vector<int> ncs;
            int nowh=vp[i].h;
            while (vp[i].h==nowh)
            {
                g[ vp[i].x ][ vp[i].y ]=1;
                sumrow[ vp[i].x ]++;
                sumcol[ vp[i].y ]++;
                if (sumrow[ vp[i].x ]==m) nrs.push_back(vp[i].x);
                if (sumcol[ vp[i].y ]==n) ncs.push_back(vp[i].y);
                i++;
            }
            i--;

            for (int k=0;k<nrs.size();k++)
            {
                for (int l=0;l<m;l++) demo[ nrs[k] ][l]=1;
            }

            for (int k=0;k<ncs.size();k++)
            {
                for (int l=0;l<n;l++) demo[l][ ncs[k] ]=1;
            }

            for (int k=0;k<n;k++)
                for (int l=0;l<m;l++)
                {
                    if (ans==false) break;
                    if (demo[k][l]!=g[k][l]) {ans=false; break;}
                }
            if (ans==false) break;
        }
        printf("Case #%d: ",cs);
        if (ans==false) cout<<"NO"<<endl;
            else cout<<"YES"<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
