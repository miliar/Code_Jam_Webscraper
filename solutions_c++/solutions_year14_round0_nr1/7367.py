#include<algorithm>
#include<iostream>
#include<iomanip>
#include<cstring>
#include<cstdlib>
#include<complex>
#include<cstdio>
#include<vector>
#include<stack>
#include<queue>
#include<cmath>
#include<deque>
#include<map>
#include<set>
#define oo 1000000000
#define ooll 1ll<<50
#define base 1000000007ll
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef vector<int> vi;
typedef vector<ii> vii;
                            /*                           END OF TEMPLATE                            */
//IOI 2014
int ans[20];
void execute()
{
    memset(ans,0,sizeof(ans));
    int x,u;
    for(int t=1; t<=2; t++)
    {
        scanf("%d",&x);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
            {
                scanf("%d",&u);
                if(i==x) ans[u]++;
            }
    }
    vector<int> res;
    for(int i=1; i<=16; i++)
        if(ans[i]==2) res.push_back(i);
    if(res.size()==1) printf("%d\n",res.back());
    if(res.size()==0) printf("Volunteer cheated!\n");
    if(res.size()>=2) printf("Bad magician!\n");
}
int main()
{
    freopen("A.inp","r",stdin);
    freopen("A.out","w",stdout);
    int test;
    scanf("%d",&test);
    for(int tc=1; tc<=test; tc++)
    {
        printf("Case #%d: ",tc);
        execute();
    }
    return 0;
}
