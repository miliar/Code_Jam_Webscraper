#include<cstdio>
#include<algorithm>

using namespace std;

int S[100000];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int t,n,s,ans;
    scanf("%d",&t);
    for ( int x=1 ; x<=t ; x++ )
    {
        ans = 0;
        scanf("%d%d",&n,&s);
        for ( int c=1 ; c<=n ; c++ )    scanf("%d",&S[c]);
        sort ( S+1 , S+1+n );
        int i=1,j=n;
        while( i <= j )
        {
            ans++;
            if ( S[i]+S[j] <= s )
            {
                i++;
            }
            j--;
        }
        printf("Case #%d: %d\n",x,ans);
    }
}
