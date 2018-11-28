#include <bits/stdc++.h>

using namespace std;

int licz[10];
long long ans[1000001];
int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin >> t;

    int all, wcase = 0;
    long long n, pom;
    int x;
    bool inf;

    while(t--)
    {
        wcase++;
        cin >> n;
        pom = n;
        all = 0;
        for(int i = 0; i < 10; i++) licz[i] = 0;
        while(pom > 0)
        {
            if(licz[pom%10] == 0){
                all++;
                licz[pom%10] = 1;
            }
            pom /= 10;
        }
        x = 1;
        inf = false;
        if(n == 0) inf = true;
        else if(!ans[n]){
            while(all < 10)
            {
                x++;
                pom = x*n;

                while(pom > 0)
                {
                    if(licz[pom%10] == 0){
                        all++;
                        licz[pom%10] = 1;
                    }
                    pom /= 10;
                }
            }
            ans[n] = x*n;
        }

        cout << "Case #" << wcase << ": ";
        if(!inf) cout << ans[n] << "\n";
        else cout << "INSOMNIA\n";
    }
}
