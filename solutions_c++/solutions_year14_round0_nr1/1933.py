#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<string>
#include<math.h>
#include<stdlib.h>
#define pb push_back
#define tr(c,i) for(typeof((c).begin() )i = (c).begin(); i != (c).end(); i++)
//typedef pair<int,int> ii;
//typedef vector< vector<pair<int,int> > > dk;
//map<string,int> m;

using namespace std;


int main()
{ freopen("A-small-attempt0.in", "r", stdin);
    freopen("outsmall0.txt", "w", stdout);
    int t,x,p,q,n,i,j,a[6][6],b[6][6],cnt;
    scanf("%d",&n);
    for(t=1;t<=n;t++)
    {
        scanf("%d",&p);
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        scanf("%d",&a[i][j]);
        scanf("%d",&q);
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        scanf("%d",&b[i][j]);
        cnt=0;
        for(j=1;j<=4;j++)
        {
            for(i=1;i<=4;i++)
            {if(a[p][j]==b[q][i])
            {
                cnt++;
                x=a[p][j];
                break;
            }
            }
        }
        if(cnt==1)
        printf("Case #%d: %d\n",t,x);
        else if(cnt>=2)
        printf("Case #%d: Bad magician!\n",t);
        else
        printf("Case #%d: Volunteer cheated!\n",t);


    }


    return 0;
}


