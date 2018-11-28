#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<iomanip>
#include<fstream>

#include<string>
#include<utility>
#include<vector>
#include<list>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>

#define ii long long int
#define pi 2*acos(0.0)
#define eps 1e-9
#define mem(x,y) memset(x,y,sizeof(x))
#define all(x) x.begin(), x.end()
#define pb push_back
#define sz(a) (int)a.size()
#define inf 2147483640
#define mx 100010

using namespace std;

const int debug= 0;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int x,t,N= 4;
    scanf("%d",&t);

    for (x=1;x<=t;++x)
    {
        int r1,r2,i,j,k,cnt=0,val;
        set <int> st;

        scanf("%d",&r1);

        for (i=1;i<=N;++i) for (j=1;j<=N;++j)
        {
            scanf("%d",&k);
            if (i==r1) st.insert(k);
        }

        scanf("%d",&r2);

        for (i=1;i<=N;++i) for (j=1;j<=N;++j)
        {
            scanf("%d",&k);
            if (i==r2 && st.find(k)!=st.end())
            {
                cnt++;
                val=k;
            }
        }

        printf("Case #%d: ",x);
        if (cnt==1) cout<<val<<endl;
        else if (cnt>1) puts("Bad magician!");
        else puts("Volunteer cheated!");
    }
    return 0;
}
