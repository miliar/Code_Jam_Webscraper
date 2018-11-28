#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <cstdlib>
using namespace std;
int R, P, S;
int n;
vector<int> ans;

void gao(int k) {
    vector<int> tmp, res;
    tmp.push_back(k);
    for(int i = 0; i < n; i++) {
        res.clear();
        for(int j = 0; j < tmp.size(); j++) {
            k = tmp[j];
            if(k == 0) {
                res.push_back(0);
                res.push_back(1);
            }
            if(k == 1) {
                    res.push_back(1);
                    res.push_back(2);
            }
            if(k == 2) {
                res.push_back(0);
                res.push_back(2);
            }
        }
        tmp.clear();
        for(int j = 0; j < res.size(); j++) tmp.push_back(res[j]);
    }
    int cnt1 = 0, cnt2 = 0, cnt3 = 0;
    for(int j = 0; j < res.size(); j++) {
        if(res[j] == 0) cnt1++;
        if(res[j] == 1) cnt2++;
        if(res[j] == 2) cnt3++;
    }
    if(cnt1 == P && cnt2 == R && cnt3 == S) {
        //for(int j = 0; j < res.size(); j++) printf("%d\n", res[j]);
        for(int i = 1; i <= n; i++) {
            int now_len = 1 << i;
            for(int j = 0; j < res.size(); j += now_len) {
                int flag = 1;
                int nt = now_len / 2;
                for(int k = 0; k < now_len/2; k++) {
                    if(res[j + k] > res[j + nt + k]) {
                        flag= 0 ;
                        break;
                    }
                }
                if(!flag) {
                    for(int k = 0; k < now_len/2; k++) {
                        swap(res[j + k], res[j + nt + k]);
                    }
                }
            }
        }
        if (ans.size() == 0) ans = res;
        else {
            int flag = 1;
            for(int i = 0; i < ans.size(); i++) {
                if(ans[i] > res[i]) {
                    flag=  0;
                    break;
                }
            }
            if(!flag) ans = res;
        }
    }
}
int main() {
    int T;
    int cas = 0;
    cin >> T;
    while(T--) {
        cin >> n >> R >> P >> S;
        ans.clear();
        for(int i = 0; i < 3; i++)
            gao(i);
        //cout << ans.size() << endl;
        printf("Case #%d: ", ++cas);
        if(ans.size() == 0) printf("IMPOSSIBLE\n");
        else {
            for(int i = 0; i < ans.size(); i++) {
                if(ans[i] == 0) putchar('P');
                if(ans[i] == 1) putchar('R');
                if(ans[i] == 2) putchar('S');
            }
            printf("\n");
        }
    }

    return 0;
}
