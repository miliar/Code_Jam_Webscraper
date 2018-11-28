#include<bits/stdc++.h>
#define ll long long int
#define pii pair<int,int>
#define mp make_pair
#define vi vector<int>
#define pb push_back
#define in(a) cin >> a
#define in2(a,b) cin >> a >> b
#define out(a) cout << a
#define outs(a) cout << a << " "
#define newl printf("\n")
#define chk(a) cout << endl << #a << " : " << a << endl
#define chk2(a,b) cout << endl << #a << " : " << a << "\t" << #b << " : " << b << endl
#define chk3(a,b,c) cout << endl << #a << " : " << a << "\t" << #b << " : " << b << "\t" << #c << " : " << c << endl
#define chk4(a,b,c,d) cout << endl << #a << " : " << a << "\t" << #b << " : " << b << "\t" << #c << " : " << c << "\t" << #d << " : " << d << endl

using namespace std;

int h[10];

bool allDone() {
    for(int i=0; i<10; i++) {
        if(h[i]==0) return 0;
    }
    return 1;
}

void checkDig(int a) {
    while(a!=0) {
        h[a%10] = 1;
        a /= 10;
    }
}

int main() {
    freopen("A-large (1).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t,tt;
    in(t);
    for(int tt=1; tt<=t; tt++) {
        int n;
        in(n);
        printf("Case #%d: ", tt);
        memset(h, 0, sizeof(h));
        if(n==0) {
            out("INSOMNIA"); newl; continue;
        }
        int i=2;
        int nOrg = n;
        while(1) {
            checkDig(n);
            if(allDone()) {
                break;
            }
            n = i*nOrg; i++;
        }
        out(n); newl;
    }
    return 0;
}
