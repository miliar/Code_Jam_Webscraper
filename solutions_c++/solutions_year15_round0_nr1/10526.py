#include<iostream>
#include<cstring>
#include<string>

using namespace std;


string ch;
int a[15];
int main()
{
    int t;
    int n;
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    while(scanf("%d", &t) !=EOF)
    {
        for(int i = 1; i <= t; i++)
        {
            int ans = 0, cnt = 0;
            scanf("%d", &n);
            cin >> ch;
            for(int j = 0; j <= n; j++)
            {
                a[j] = ch[j] - '0';
            }
            ans = a[0];

            for(int j = 1; j <= n; j++)
            {


                while(ans < j)
                {
                    cnt++;
                    ans++;
                }
                ans += a[j];
            }
            cout << "Case #" << i << ": " << cnt << endl;
            ans = 0;
            cnt = 0;
        }

    }
    return 0;
}
