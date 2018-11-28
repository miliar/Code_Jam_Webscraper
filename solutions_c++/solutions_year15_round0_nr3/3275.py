#include<bits/stdc++.h>

using namespace std;

vector<int> li;

char ok[10*1000+5];

int kali(int a, int b) {
    int neg = 1;
    if(a < 0 && b < 0) {
        a*=-1;
        b*=-1;
    } else if(a < 0 || b < 0) {
        a = abs(a);
        b = abs(b);
        neg = -1;
    }
    if(a == 1 || b == 1) {
        return a * b * neg;
    }
    if(a == 'i') {
        if(b == 'i') {
            return -1 * neg;
        }
        if(b == 'j') {
            return 'k' * neg;
        }
        if(b == 'k') {
            return -1 * 'j' * neg;
        }
    }
    if(a == 'j') {
        if(b == 'i') {
            return -1 * 'k' * neg;
        }
        if(b == 'j') {
            return -1 * neg;
        }
        if(b == 'k') {
            return 'i' * neg;
        }
    }
    if(a == 'k') {
        if(b == 'i') {
            return 'j' * neg;
        }
        if(b == 'j') {
            return -1 * neg * 'i';
        }
        if(b == 'k') {
            return -1 * neg;
        }
    }
    return 0;
}

int dp[10*1000][10*1000];

void solve() {
    li.clear();

    int n, x;
    scanf("%d%d", &n,&x);

    scanf("%s", ok);

    string sok = "";

    for(int i =0 ; i < x; i++) {
        for(int j =0; j < n; j++) {
            int v = (int)ok[j];
            //sok += ok[j];
            li.push_back(v);
        }
    }


    if(li.size() < 3) {
        printf("NO\n");
        return;
    }

    for(int i =0 ; i < (int)li.size(); i++) {
        int cu = 1;
        for(int j = i ; j < (int)li.size(); j++) {
            cu = kali(cu,li[j]);
            dp[i][j] = cu;
        }
    }

    int left = 1;
    for(int i = 0; i<(int)li.size()-2; i++) {
        left = kali(left,li[i]);
        int tengah = 1;
        for(int j = i+1; j < (int) li.size()-1; j++) {
            tengah = kali(tengah, li[j]);
            int kanan = dp[j+1][li.size()-1];

            //cout << sok.substr(0,i+1) << ' ' << sok.substr(i+1,j-i) << ' ' << sok.substr(j+1,sok.length()-j-1) << '\n';
            //cout << left << ' ' << tengah << ' ' << kanan << '\n';
            if(left == 'i' && tengah == 'j' && kanan == 'k') {
                printf("YES\n");
                return;
            }
        }
    }
    printf("NO\n");

}

int main() {
    int tc;
    scanf("%d", &tc);
    for(int i = 1; i<=tc; i++) {
        printf("Case #%d: ",i);
        solve();
    }
}