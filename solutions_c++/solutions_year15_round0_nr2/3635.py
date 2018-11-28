#include <bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int caso=1; caso<=t; caso++)
    {
        int n;
        scanf("%d",&n);

        int vet[n], maximo=0;
        for(int i=0; i<n; i++) scanf("%d",&vet[i]), maximo = max(maximo, vet[i]);

        int ans = 0x3f3f3f3f;

        for(int k=1; k<=maximo; k++)
        {
            int local = k;
            for(int i=0; i<n; i++)
            {
                if(vet[i] > k)
                {
                    local += (vet[i]/k);
                    if(vet[i]%k == 0) local--;
                }
            }
            ans = min(ans,local);
        }
        printf("Case #%d: %d\n",caso,ans);
    }
    return 0;
}
