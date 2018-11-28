#include <iostream>
#include<cstdio>

using namespace std;

int main()
{
    unsigned long long int a, b, k, t;
    cin>>t;
    for (int tc=1; tc<=t; tc++)
    {
        unsigned long long ans = 0;
        cin >> a >> b >> k;
        for (int i=0; i<a; i++)
        {
            for (int j=0; j<b; j++)
            {
                if ((i&j) < k)
                {
                    ans++;
                }
            }
        }
        printf("Case #%d: ",tc);
        cout << ans << endl;
    }
    return 0;
}
