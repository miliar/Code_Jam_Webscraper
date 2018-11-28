#include<stdio.h>
#include<string.h>
#include<vector>
#include<utility>
#include<algorithm>
using namespace std;
int a,b,c,d,e,f,g,h,i,j;
int zz[105][105];
vector<pair<int, pair<int,int> > > v;
pair<int, pair<int,int> > p;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&a);
    for (b=1;b<=a;b++)
    {
        scanf("%d %d",&c,&d);
        for (e=1;e<=c;e++)
        {
            for (f=1;f<=d;f++)
            {
                scanf("%d",&zz[e][f]);
                v.push_back(make_pair(zz[e][f],make_pair(e,f)));
            }
        }

        sort(v.begin(),v.end());

        for (e=0;e<v.size();e++)
        {
            if (zz[v[e].second.first][v[e].second.second]==v[e].first)
            {
                g=1;
                for (i=1;i<=c;i++)
                    if (zz[i][v[e].second.second]!=v[e].first && zz[i][v[e].second.second]!=101)
                    {
                        g=0;
                        break;
                    }
                if (g==1)
                for (i=1;i<=c;i++)
                    zz[i][v[e].second.second]=101;

                g=1;
                for (i=1;i<=d;i++)
                    if (zz[v[e].second.first][i]!=v[e].first && zz[v[e].second.first][i]!=101)
                    {
                        g=0;
                        break;
                    }
                if (g==1)
                for (i=1;i<=d;i++)
                    zz[v[e].second.first][i]=101;
            }
        }

        g=1;
        for (e=1;e<=c;e++)
            for (f=1;f<=d;f++)
                if (zz[e][f]!=101)
                {
                    g=0;
                    break;
                }

        printf("Case #%d: ",b);
        if (g==1)
            printf("YES\n");
        else
            printf("NO\n");

    }
    return 0;
}
