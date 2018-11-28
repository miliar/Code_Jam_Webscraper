#include<bits/stdc++.h>
using namespace std;


int n;
int a[20000];
int ans1 = 0,ans2 = 0;

int main(){
    int test_case = 0,test_tot;
    cin >> test_tot;
    for (int test_case = 1;test_case <= test_tot;++test_case){
        cin >> n;
        for (int i = 1;i <= n;++i) cin >> a[i];
        ans1 = ans2 = 0;

        //first
        for (int i = 2;i <= n;++i)
            if (a[i] < a[i - 1])
            ans1 += a[i - 1] - a[i];


        //second
        int maxd = 0;
        for (int i = 2;i <= n;++i)
            if (a[i] < a[i - 1])
            maxd = max(maxd,a[i - 1] - a[i]);
        for (int i = 1;i <= n - 1;++i)
            if (a[i] >= maxd)
            ans2 += maxd;
                else
            ans2 += a[i];
        cout << "Case #" << test_case << ": " << ans1 << " " << ans2 << endl;
    }
    return 0;
}
