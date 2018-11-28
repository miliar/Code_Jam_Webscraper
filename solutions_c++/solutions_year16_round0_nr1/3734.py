#include <bits/stdc++.h>
using namespace std;
bool seen[10];
int cnt;
void process(long long x)
{
    while(x)
    {
        if(seen[x%10]==false) cnt++;
        seen[x%10]=true;
        x/=10;
    }
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++){
        int n;
        scanf("%d",&n);
        for(int i=0;i<10;i++)
            seen[i]=false;
        cnt=0;
        cout << "Case #" << test << ": ";
        if(n==0) cout << "INSOMNIA" << endl;
        else {
            int ans=1;
            for(;cnt<10;ans++) process(1ll*n*ans);
            printf("%lld\n",1ll*n*(ans-1));
        }
    }
    return 0;
}
