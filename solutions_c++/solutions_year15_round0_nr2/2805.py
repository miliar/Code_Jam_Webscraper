#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
string str;

int p[1100];
int main()
{
    //freopen("B-small-attempt0.in","r",stdin);
    //freopen("B-small-attempt0.out","w",stdout);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    cin>>T;
    int cas = 1;
    while (T--) {
        int n;
        scanf("%d",&n);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            cin>>p[i];
        }
        sort(p, p + n);
        ans = p[n - 1];
        for (int i = 1; i <= p[n - 1]; i++) {
            int tmp_ans = i;
            for (int j = 0; j < n; j++) {
                tmp_ans += (p[j] - 1) / i;
            }
            ans = min(ans,tmp_ans);
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
}
