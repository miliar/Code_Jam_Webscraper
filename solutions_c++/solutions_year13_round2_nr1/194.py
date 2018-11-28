#include<iostream>
#include<sstream>
#include<cstdio>
#include<cctype>
#include<string>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<vector>
#include<cstring>
#include<algorithm>

#define ll long long
#define inf 1000000009
#define mod 1000000007

using namespace std;

typedef pair<int,int> II;
int n,A,a[109];
void go(int cas)
{    
    cin>>A>>n;
    for(int i=0;i<n;i++) cin>>a[i];
    if(A==1)
    {
        printf("Case #%d: %d\n",cas,n);
        return;
    }
    sort(a,a+n);
    int res=n,tmp=0;
    for(int i=0;i<n;i++)
    {
        while(A<=a[i]) A+=A-1,tmp++;
        A+=a[i];
        res=min(res,tmp+n-i-1);
    }
    printf("Case #%d: %d\n",cas,res);
}

int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int T;
    cin>>T;
    for(int run=1;run<=T;run++) go(run);
    fclose(stdout);
}
