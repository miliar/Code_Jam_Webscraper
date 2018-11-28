#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    scanf("%d",&t);
    for(int caso=1; caso<=t; caso++)
    {
        int sm;
        scanf("%d",&sm);

        string s;
        cin >> s;

        int acc=0, ans=0;

        if(s[0] == 0) ans = acc = 1;
        else acc = s[0]-'0';

        for(int i=1; i<=sm; i++)
        {
            s[i] -= '0';
            if(s[i] != 0 && acc < i) ans += (i-acc), acc = i;
            acc += s[i];
        }

        printf("Case #%d: %d\n",caso, ans);
    }
    return 0;
}
