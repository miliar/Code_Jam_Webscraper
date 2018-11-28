#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

bool cmp(const PII &a, const PII &b){
    return a.first > b.first;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t,n;
    cin >> t;
    string na = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    for(int test = 1;test <= t; test++){

        cin >> n;

        PII p[n];
        int cur = 0;
        printf("Case #%d: ", test);
        for(int i=0;i<n;i++){
            cin >> p[i].first;
            p[i].second = i;
            cur+=p[i].first;
        }

        while(cur > 0){
            sort(p, p+n, cmp);

            if( p[1].first < (cur - 2) / 2 ){
                cout << na[ p[0].second ] << na[ p[0].second ] << ' ';
                cur-=2;
                p[0].first-=2;
                continue;
            }

            if( p[1].first < (cur - 1) / 2 || cur % 2 == 1){
                cout << na[ p[0].second ] << ' ';
                cur--;
                p[0].first--;
                continue;
            }

            cout << na[ p[0].second ] << na[ p[1].second ] << ' ';
            cur-=2;
            p[0].first--;
            p[1].first--;
        }

        cout << endl;

    }

    return 0;
}
