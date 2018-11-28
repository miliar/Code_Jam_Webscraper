#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0) ;
    freopen("B-large.in","r",stdin) ;
    freopen("B-large.out","w",stdout) ;
    int t, cs = 1 ;
    cin >> t ;
    while(t--)
    {
        string pancakes ;
        cin >> pancakes ;
        int ans = 0 ;
        for(int i=0;i<pancakes.size();i++)
        {
            if(pancakes[i]!=pancakes[0])
            {
                ans++ ;
                for(int j=0;j<i;j++)
                {
                    if(pancakes[j]=='+')
                        pancakes[j] = '-' ;
                    else
                        pancakes[j] = '+' ;
                }
            }
        }
        if(pancakes[0]=='-')
            ans++ ;
        cout << "Case #" << cs << ": " << ans << endl ;
        cs++ ;
    }
    return 0;
}
