#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <set>
#include <algorithm>
#include <map>
#include <bitset>
#include <vector>
#include <queue>
#include <stack>
#include <utility>
#include <functional>
#include <sstream>
#include <list>
#include <complex>
#include <ctime>

#define maxlongint 2147483647
#define biglongint 2139062143
#define LL long long
#define ULL unsigned long long
#define p_b push_back
#define m_p make_pair
#define l_b lower_bound
#define w1 first
#define w2 second

using namespace std;

typedef pair<int,int> PII;
typedef pair<pair<int,int>,int> PIII;
typedef pair<pair<int,int>,pair<int,int> > PIIII;
typedef pair<double,double> PDD;
typedef pair<double,int> PDI;
typedef pair<string,int> PSI;
typedef pair<pair<double,double>,double> PDDD;
typedef pair<pair<double,double>,pair<double,double> > PDDDD;

int TT,xc,yc,a[5][5],b[5][5];
vector<int> ans;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);

    scanf("%d",&TT);
    for (int gb=1;gb<=TT;gb++)
    {
        scanf("%d",&xc);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&yc);
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                scanf("%d",&b[i][j]);
        ans.clear();
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                if (a[xc][i]==b[yc][j]) ans.p_b(a[xc][i]);
        printf("Case #%d: ",gb);
        if (ans.size()==0) printf("Volunteer cheated!\n"); else
        if (ans.size()==1) printf("%d\n",ans[0]); else
        printf("Bad magician!\n");
    }

    return 0;
}
