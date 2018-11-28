#include <bits/stdc++.h>

using namespace std;

int T,N;

int main()
{
    scanf("%d",&T);
    for(int i = 1; i<=T; ++i)
    {
        vector<bool> check(10,false);
        scanf("%d",&N);
        if( !N ) { printf("Case #%d: INSOMNIA\n",i); continue; }
        int n = N, factor = 1;
        bool conti = true;
        while(conti)
        {
            while( n > 0 )
            {
                check[n%10] = true;
                n = (n-n%10)/10;
            }
            n = N*(++factor);
            conti = false;
            for(int j = 0; j<10; ++j)
                if( !check[j] ) conti = true;
        }
        printf("Case #%d: %d\n",i,(N*(factor-1)));
    }
}


