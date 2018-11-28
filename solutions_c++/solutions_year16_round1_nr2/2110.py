//OUM HARI OUM, OUM TATSAT
// OUM NAMA VAGABATE BASUDEBAY
// OUM NAMA MA SWARASATI OUM NAMA

#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<stdlib.h>
#include<iostream>
#include<algorithm>

#define cl(vctr) vctr.clear()
#define ms(v, ar) memset(ar, v, sizeof(ar))

const double pi=(double)(2.0 * acos( 0.0 ));
const int inf=1 << 30;
const double eps=1E-9;
const double e = exp(1.0);
const int sz=100000 + 5;
const int mod=1000000000 + 7;

using namespace std;
typedef long long int ll;

int cnt[3005];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("Bout.in","w",stdout);
    int t,T,i,j,ai,n;
    scanf("%d",&t);T=t;
    while(t--)
    {
        ms(0,cnt);
        scanf("%d",&n);
        for(i=0;i<2*n-1;i++)
        {
            for(j=0;j<n;j++)
            {
                scanf("%d",&ai);
                cnt[ai]++;
            }
        }
        vector<int> v;
        v.clear();
        for(i=0;i<3000;i++)
        {
            if(cnt[i]&1) v.push_back(i);
        }
        sort(v.begin(),v.end());
        printf("Case #%d:",T-t);
        for(i=0;i<n;i++)
        {
            printf(" %d",v[i]);
        }
        printf("\n");
    }

    return 0;
}
