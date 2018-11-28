#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <utility>
#include <sstream>
#include <algorithm>
using namespace std;
#define ll long long
const long long LINF = ~(((long long)0x1)<<63)/2;
const int INF=0X3F3F3F3F;
const double eps=1e-7;
int a[110][110];
int r[110],c[110];
int main()
{
    freopen("B-large.in.txt","r",stdin);
    freopen("B-large.out.txt", "w", stdout);
    int T,n,m;
    cin>>T;
    for(int cas=1;cas<=T;cas++)
    {
        vector<pair<int,pair<int,int> > > p;
        cin>>n>>m;
        printf("Case #%d: ",cas);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                scanf("%d",&a[i][j]);
                p.push_back(make_pair(a[i][j], make_pair(i,j)));
            }
        sort(p.begin(),p.end());
        bool flag=true;
        for(int i=0;i<p.size();i++)
        {
            int x=p[i].second.first;
            int y=p[i].second.second;
            int v=p[i].first;
            if(r[x]==v||c[y]==v) continue;
            bool mark=true;
            for(int j=0;j<m;j++)
                if(a[x][j]>v) mark=false;
            if(mark) continue;
            mark=true;
            for(int j=0;j<n;j++)
                if(a[j][y]>v) mark=false;
            if(!mark)
            {
                flag=false;
                break;
            }
        }
        if(flag)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
        
    }
    return 0;
}











