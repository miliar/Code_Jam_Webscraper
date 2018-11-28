#include<iostream>
#include<fstream>
#include<cstring>
#include<stdio.h>
#include<assert.h>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define F first
#define S second
#define ll long long
#define pp pair<int,int>
#define SS system("pause")
#define INF 1000000000
#define dd double
#define vec vector<int>::iterator
using namespace std;
const int N=1006;
int T,t,i,j,ans,n,x,a[N],cnt;


int main()
{freopen("B-large.in","r",stdin);
 freopen("Bout.txt","w",stdout);
 scanf("%d",&T);
 for(t=1;t<=T;t++){
    scanf("%d",&n);
    ans=INF;
    for(i=1;i<=n;i++)scanf("%d",&a[i]);

    for(x=1;x<=1000;x++){
        cnt=0;
        for(i=1;i<=n;i++)cnt+=(a[i]-1)/x;
        ans=MIN(ans,cnt+x);
    }

    cout<<"Case #"<<t<<": "<<ans<<endl;
 }
 return 0;
}
