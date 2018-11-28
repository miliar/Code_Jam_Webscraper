#include<bitset>
#include<map>
#include<vector>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<queue>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, N) for (int I = 0; I < (N); ++I)
#define REPP(I, A, B) for (int I = (A); I < (B); ++I)
#define REPC(I, C) for (int I = 0; !(C); ++I)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define RS(X) scanf("%s", (X))
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
#define MP make_pair
#define PB push_back
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define LEN(X) strlen(X)
#define F first
#define S second
#define ULL unsigned long long
#define SLL long long
using namespace std;

int N;
string find_std(string &in)
{
    string ans = "";
    ans += in[0];
    REPP(i, 1, in.length()) {
        if(in[i]!=in[i-1]) ans += in[i];
    }
    return ans;
}

int find_min(vector<string> &wds, string &st) {
    int ans = 0;
    vector<int> idx(N, 0);
    REP(i, st.length()) {
        vector<int> evc(N, 0);
        int cnt = 0;
        REP(j, idx.size()) {
            while(wds[j][idx[j]]==st[i]) {
                evc[j]++;
                cnt++;
                ++idx[j];
            }
        }
        int ave = floor(cnt/(double)N + 0.5);
        REP(j, N) {
            ans +=abs(evc[j]-ave);
        }
    }
    return ans;
}

int main()
{
    CASET {
        RI(N);
        vector<string> wds(N, "");
        vector<int> cms;
        
        REP(i, N) {
            cin >> wds[i];            
        }
        string st = find_std(wds[0]);
        bool fl = false;
        REPP(i, 1, wds.size()) {
            string stt = find_std(wds[i]);
            if(stt!=st) fl = true;
        }
        printf("Case #%d: ", case_n);
        if(fl==true) printf("Fegla Won\n");
        else printf("%d\n", find_min(wds, st));
        ++case_n;
    }
    return 0;
}
