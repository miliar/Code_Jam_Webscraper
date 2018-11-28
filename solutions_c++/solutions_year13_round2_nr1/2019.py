#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long LL;

LL mot[105];


LL need_times(LL & A,LL mt)
{
    LL ans = 0;
    while(A <= mt)
    {
        A = A + (A - 1);
        ans++;
    }
    return ans;
}
int main()
{
    freopen("AL1.in","r",stdin);
    freopen("AL1.out","w",stdout);
    LL ca,cn,A,N,i;

    cin >> cn;

    for(ca = 1;ca <= cn;ca++)
    {
        cin >> A >> N;

        for(i = 0;i < N;i++)
            cin >> mot[i];

        sort(mot,mot + N);

        LL ans = N,cur = 0;
        for(i = 0;i < N;i++)
        {
            if(A > mot[i])
            {
                A += mot[i];
                if(cur + (N - i - 1) < ans)
                    ans = cur + (N - i - 1);
            }
            else
            {
                LL nt = 0;
                if(A == 1)
                    nt = 10000;
                else
                    nt = need_times(A,mot[i]);

                cur += nt;
                A += mot[i];

                if(cur + (N - i - 1) < ans)
                    ans = cur + (N - i - 1);
            }
        }

        cout << "Case #"<< ca <<": " << ans << endl;
    }
    return 0;
}
