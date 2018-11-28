#include <bits/stdc++.h>
#define ull unsigned long long

using namespace std;

char v[1000000];
string a, b, c;

void build (int i, int r){
    if (!r) return;
    if (v[i] == 'R'){
        v[i*2] = 'R';
        v[i*2+1] = 'S';
    }

    if (v[i] == 'R' && r>1){
        v[i*2] = 'S';
        v[i*2+1] = 'R';
    }

    if (v[i] == 'P'){
        v[i*2] = 'P';
        v[i*2+1] = 'R';
    }

    if (v[i] == 'S'){
        v[i*2] = 'P';
        v[i*2+1] = 'S';
    }

    if (v[i] == 'S' && r > 2){
        v[i*2] = 'S';
        v[i*2+1] = 'P';
    }

    build (i*2, r -1);
    build (i*2+1, r-1);

}

string get (int r, int p, int s, int n, char b){
    string ans;
    v[1] = b;
    build(1, n);
    for (int i = (1<<n); i < (1<<(n+1)); i++){
        ans += v[i];
        if (v[i] == 'R') r--;
        if (v[i] == 'P') p--;
        if (v[i] == 'S') s--;
    }
    //cout << ans << endl;
    return (r==0&&p==0&&s==0?ans:"");
}

int main(){
    int tt;
    scanf ("%d", &tt);

    for (int cc = 1; cc <= tt; cc++){



        int n, r, p, s;
        scanf ("%d %d %d %d", &n, &r, &p, &s);

        string ans = "";

        string a = get (r, p, s, n, 'R');
        if (ans == "") ans = a;
        if (ans != "" && ans > a && a != "") ans = a;

        a = get (r, p, s, n, 'P');

        if (ans == "") ans = a;
        if (ans != "" && ans > a && a != "") ans = a;

        a = get (r, p, s, n, 'S');
        if (ans == "") ans = a;
        if (ans != "" && ans > a && a != "") ans = a;

        printf ("Case #%d: ", cc);
        if (ans == "") ans = "IMPOSSIBLE";
        cout << ans << endl;
    }

    return 0;
}
