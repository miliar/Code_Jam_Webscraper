
#include <cstdio>
#include <cstring>
#include <iostream>
#define ll long long
using namespace std;
const int maxn = 10000 + 5;
ll a[maxn],n,m,k;

int main() {
    int T;
    cin>>T;
    for (int t = 1; t <= T; t++) {
        printf("Case #%d:\n",t);
        cin>>n>>m>>k;
        for (int i = 0; i < n; i++) {
            scanf("%I64d",&a[i]);
            //cin>>a[i];
        }
        sort(a,a+n);
        int tmp = -2;
        for (int i = 0; i < n; i++) {
            if (a[i] > m) {
                tmp = i - 1;
                break;
            }
        }
        //cout<<tmp<<endl;
        if (tmp == -1) {
            cout<<"madan!"<<endl;
            continue;
        }
        else if (tmp == -2) {
            cout<<"why am I so diao?"<<endl;
            continue;
        }
        else {
            ll att = a[tmp];
            bool flag = true;
            for (int i = tmp+1; i < n; i++) {
                if (att + max(k,0LL) < a[i]) {
                    flag = false;
                    break;
                }
                else {
                    att = a[i];
                    k--;
                }
            }
            if (flag) cout<<"why am I so diao?"<<endl;
            else cout<<"madan!"<<endl;
        }
    }
}