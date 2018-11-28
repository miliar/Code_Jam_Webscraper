#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);

    ios::sync_with_stdio(0);
    int t; cin >> t;
    for(int test=1; test<=t; ++test)
    {
        string a;
        cin >> a;

        int cnt=0, i=0;
        long long num=0, dem=0;
        while(a[i]!='/')
            num = (10*num) + (a[i++]-48);
        i++;
        while(i<a.size())
            dem = 10*dem + (a[i++]-48);

        if(dem%2 && num!=dem)
            cout << "Case #" << test << ": " << "impossible\n";
        else
        {
            //while(num%2==0)num/=2;

            while(dem>num && dem%2==0){
                //if(num%2==0)num/=2;
                dem/=2; cnt++;
            }

            if(dem%2 && num!=dem)
                cout << "Case #" << test << ": " << "impossible\n";
            else
                cout << "Case #" << test << ": " << cnt << '\n';
        }
    }
    return 0;
}
