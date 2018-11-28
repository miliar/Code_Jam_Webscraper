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

int a[20][20];
int tt,flag,ee;
string s[10];

void check(int x1,int y1,int x2,int y2,int x3,int y3,int x4,int y4)
{
    if (
        ((a[x1][y1]==1)||(a[x1][y1]==-1))
      &&((a[x2][y2]==1)||(a[x2][y2]==-1))
      &&((a[x3][y3]==1)||(a[x3][y3]==-1))
      &&((a[x4][y4]==1)||(a[x4][y4]==-1))
        )
            flag=1;
    if (
        ((a[x1][y1]==2)||(a[x1][y1]==-1))
      &&((a[x2][y2]==2)||(a[x2][y2]==-1))
      &&((a[x3][y3]==2)||(a[x3][y3]==-1))
      &&((a[x4][y4]==2)||(a[x4][y4]==-1))
        )
            flag=2;
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);

    scanf("%d",&tt);
    for (int gb=1;gb<=tt;gb++)
    {
        for (int i=1;i<=4;i++) cin>>s[i];
        memset(a,0,sizeof(a));
        for (int i=1;i<=4;i++)
            for (int j=1;j<=4;j++)
                if (s[i][j-1]=='T') a[i][j]=-1; else
                if (s[i][j-1]=='O') a[i][j]=1; else
                if (s[i][j-1]=='X') a[i][j]=2;
        flag=0;
        check(1,1,1,2,1,3,1,4);
        check(2,1,2,2,2,3,2,4);
        check(3,1,3,2,3,3,3,4);
        check(4,1,4,2,4,3,4,4);
        check(1,1,2,1,3,1,4,1);
        check(1,2,2,2,3,2,4,2);
        check(1,3,2,3,3,3,4,3);
        check(1,4,2,4,3,4,4,4);
        check(1,1,2,2,3,3,4,4);
        check(1,4,2,3,3,2,4,1);
        cout<<"Case #"<<gb<<": ";
        if (flag==1) cout<<"O won"<<endl; else
        if (flag==2) cout<<"X won"<<endl; else
        {
            ee=1;
            for (int i=1;i<=4;i++)
                for (int j=1;j<=4;j++)
                    if (a[i][j]==0) ee=0;
            if (ee==1) cout<<"Draw"<<endl; else cout<<"Game has not completed"<<endl;
        }
    }

    return 0;
}
