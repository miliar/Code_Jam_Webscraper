#include <bits/stdc++.h>
using namespace std;

bool flag[10];
void Gao(int num)
{
    for(;num;num/=10) flag[num%10]=true;
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, ca = 1;
    cin >> T;
    while(T--) {
        int n;
        cin >> n;
        int ret = -1;
        memset(flag, false, sizeof(flag));
        for(int i = 1; i <= 1000; i++) {
            int num = n * i;
            Gao(num);
            bool yes = true;
            for(int j = 0; j < 10; j++) {
                if(!flag[j]) {
                    yes = false;
                }
            }
            if(yes) {
                ret = num;
                break;
            }
        }
        cout << "Case #" << ca << ": " ;
        if(ret == -1) cout << "INSOMNIA" << endl;
        else cout << ret<< endl;
        ca++;
    }
    return 0;
}
