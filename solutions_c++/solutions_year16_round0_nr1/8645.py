#include <bits/stdc++.h>

using namespace std;
int chk[10];

int main()
{
    freopen("dip2.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T,i,j;
    long int N,k;
    long long int cur,temp,ans;

    cin >> T;

    for(i = 1; i <= T; i++)
    {
        for(j = 0; j < 10; j++) chk[j] = 0;

        k = 0;

        cin >> N;

        if(N == 0)
        {
            cout << "Case #" << i << ": " << "INSOMNIA\n";
            continue;
        }

        while(1)
        {
            int flag = 0;

            for(j = 0; j < 10; j++)
            {
                if(chk[j] == 0)
                {   
                    flag = 1;
                    break;
                }
            }

            if(flag != 1) break;
            k++;

            temp = k*N;

            while(temp != 0)
            {
                chk[temp%10] = 1;
                temp = temp/10;

            }

            ans = k*N;
        }

        cout << "Case #" << i << ": " << ans << endl;
    }

    return 0;
}

