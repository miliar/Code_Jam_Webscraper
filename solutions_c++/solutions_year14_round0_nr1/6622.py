//#include <bits/stdc++.h>
//#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <vector>
#include <algorithm>
#include <cctype>
#include <fstream>
#include <map>
#include <list>
#include <set>
#include <string>
#include <stack>
#include <bitset>

#define sz 5
#define pb(a) push_back(a)
#define pp pop_back()
#define ll long long
#define fread freopen("A-small-attempt0.in","r",stdin)
#define fwrite freopen("output.txt","w",stdout)
#define inf (1e9)
#define chng(a,b) a^=b^=a^=b;
#define clr(abc,z) memset(abc,z,sizeof(abc))
#define PI acos(-1)
#define fr(i,a,b) for(i=a;i<=b;i++)
#define print1(a)    cout<<a<<endl
#define print2(a,b) cout<<a<<" "<<b<<endl
#define print3(a,b,c) cout<<a<<" "<<b<<" "<<c<<endl
#define mod 1000000007
using namespace std;

int a[sz][sz], b[sz][sz];


int main()
{
#ifdef ENAM
    fread;
    fwrite;
#endif // ENAM
    int t, n, m, cas=1;
    vector<int>v;
    scanf("%d", &t);

    while(t--)
    {
        scanf("%d", &n);
        for (int i = 0; i<4; i++)
            for (int j = 0; j<4; j++)
                scanf("%d", &a[i][j]);

        scanf("%d", &m);
        for (int i = 0; i<4; i++)
            for (int j = 0; j<4; j++)
                scanf("%d", &b[i][j]);

        for (int i = 0; i<4; i++)
            for (int j = 0; j<4; j++)
                if(a[n-1][i]==b[m-1][j])
                {
                    v.pb(a[n-1][i]);
                    break;
                }

        if(v.size()==0) printf("Case #%d: Volunteer cheated!\n",cas++);
        else if(v.size()==1) printf("Case #%d: %d\n",cas++,v[0]);
        else printf("Case #%d: Bad magician!\n",cas++);

        v.clear();

    }


    return 0;
}
