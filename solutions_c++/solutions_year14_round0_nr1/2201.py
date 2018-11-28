#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<iomanip>
#include<bitset>
#include<sstream>
#include<fstream>
#define debug puts("-----")
#define pi (acos(-1.0))
#define eps (1e-8)
#define inf (1<<30)
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t;
    cin>>t;
    int cas=0;
    while(t--)
    {
        int a[10][10],b[10][10];
        int q,w;
        cin>>q;
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++)
                scanf("%d",&a[i][j]);
        cin>>w;
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++)
                scanf("%d",&b[i][j]);
        int ans=0;
        int g;
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++)
            {
                if (a[q][i]==b[w][j])
                    ans++,g=a[q][i];
            }
        printf("Case #%d: ",++cas);
        if (ans==0)
            puts("Volunteer cheated!");
        else if (ans==1)
            printf("%d\n",g);
        else
            puts("Bad magician!");
    }
    return 0;
}
