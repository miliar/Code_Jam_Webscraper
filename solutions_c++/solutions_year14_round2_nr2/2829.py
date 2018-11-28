#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B_small.txt","w",stdout);
    int test, Case=0;
    scanf("%d",&test);

    while(test--){
        int a, b, k;
        scanf("%d %d %d",&a, &b, &k);
        long long int ans=0;

        for(int i=0 ; i<a ; i++) {
            for(int j=0 ; j<b ; j++) {
                int p = i&j;
                if( p < k) ans++;
            }
        }

        printf("Case #%d: %d\n",++Case,ans);
    }

    return 0;
}


