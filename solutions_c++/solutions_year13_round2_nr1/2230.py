#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main()
{
    int t, a, n, ret, f=0, v;
    int m[1000100];
    cin >> t;
    for(int i=0;i<t;i++)
    {
        cin >> a >> n;
        for(int j=0;j<n;j++) cin >> m[j];
        sort(m,m+n);
        f = 0;
        ret = 0;
        for(int j=0;j<n;j++)
        {
            v = 0;
            while(a <= m[j])
            {
                a += (a-1);
                v += 1;
                if(v >= (n-j))
                {
                    v = (n-j);
                    f = 1;
                    break;
                }
            }
            ret += v;
            if(f) break;
            a += m[j];
        }
        cout << "Case #" << i+1 << ": " << ret << endl;
    }
    return 0;
}
