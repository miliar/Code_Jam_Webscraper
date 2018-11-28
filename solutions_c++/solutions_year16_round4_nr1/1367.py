#include <bits/stdc++.h>
using namespace std;

#define PB push_back

vector<vector<string> > base(vector<int> W){
    vector<vector<string> > L;
    vector<string> X;
    X.clear();
    for (int j = 0; j < W[0]; j++) X.push_back("P");
    L.push_back(X);
    X.clear();
    for (int j = 0; j < W[1]; j++) X.push_back("R");
    L.push_back(X);
    X.clear();
    for (int j = 0; j < W[2]; j++) X.push_back("S");
    L.push_back(X);
    return L;
}

void solve(){
    int n, r, p, s;
    scanf("%d%d%d%d", &n, &r, &p, &s);
    vector<int> W = {p, r, s};
    // string res = run(W);
    vector<vector<string> > L = base(W);
    //printf("%d, %d\n", W[0], W[1]);
    vector<vector<string> > newL(3, vector<string>());
    vector<string> X;
    while (n > 0){
        vector<int> nw(3);
        int sum = W[0] + W[1] + W[2];
        //printf("-->    %d, %d, %d\n", W[0], W[1], W[2]);
        nw[0] = sum / 2 - W[2];
        nw[1] = sum / 2 - W[0];
        nw[2] = sum / 2 - W[1];
        if (nw[0] >= 0 && nw[1] >= 0 && nw[2] >= 0){
            for (int i = 0; i < 3; i++){
                reverse(L[i].begin(), L[i].end());
            }
            //PR
            X.clear();
            for (int i = 0; i < nw[0]; i++){
                string s1 = L[0].back(); L[0].pop_back();
                string s2 = L[1].back(); L[1].pop_back();
                if (s1 < s2) X.push_back(s1 + s2);
                else X.push_back(s2 + s1);
            }
            newL[0] = X;
            //PS
            X.clear();
            for (int i = 0; i < nw[2]; i++){
                string s1 = L[0].back(); L[0].pop_back();
                string s2 = L[2].back(); L[2].pop_back();
                if (s1 < s2) X.push_back(s1 + s2);
                else X.push_back(s2 + s1);
            }
            newL[2] = X;
            //RS
            X.clear();
            for (int i = 0; i < nw[1]; i++){
                string s1 = L[1].back(); L[1].pop_back();
                string s2 = L[2].back(); L[2].pop_back();
                if (s1 < s2) X.push_back(s1 + s2);
                else X.push_back(s2 + s1);
            }
            newL[1] = X;
            L = newL;
            W = nw;
        }
        else{
            printf("IMPOSSIBLE\n"); return;
        }
        //for (int i = 0; i < L.size(); i++){ for (int j = 0; j < L[i].size(); j++) printf("%s,", L[i][j].c_str()); printf("\n"); printf(".."); }
        n--;
    }
    for (int i = 0; i < L.size(); i++)
        for (int j = 0; j < L[i].size(); j++) printf("%s", L[i][j].c_str());
    printf("\n");
}

int main(){
    freopen("A-large.in", "r", stdin);
    //freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int t; scanf("%d", &t);
    for (int i = 1; i <= t; i++){
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
