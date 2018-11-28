#include <bits/stdc++.h>
using namespace std;

int T;

int N, R, P, S;

struct state{
    int p;
    int r;
    int s;
};
string order(string t, int n){
    string t1, t2;
    t1 = t;
    for (int i = 1; i<n; i*=2){
        t2 = "";
        for(int j = 0; j<t1.length(); j+=2*i){
            if (t1.substr(j, i) < t1.substr(j+i, i)){
                t2 += t1.substr(j,i) + t1.substr(j+i, i);
            }
            else{
                t2 += t1.substr(j+i, i) + t1.substr(j, i);
            }
        }
        t1 = t2;
    }
    return t1;
}
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas<=T; cas++){
        printf("Case #%d: ", cas);

        scanf("%d%d%d%d", &N, &R, &P, &S);
        int n = 1 << N;

        state st = (state){1,0,0};
        string t = "P";
        int k = 0;
        while (st.p + st.r + st.s < n){
            int np = st.p + st.s;
            int nr = st.r + st.p;
            int ns = st.s + st.r;
            st.p = np;
            st.r = nr;
            st.s = ns;
            string t2 = "";
            for(int i = 0; i<t.size(); i++){
                if (t[i] == 'P'){
                    t2 += "PR";

                }
                if (t[i] == 'R'){
                    t2 += "RS";

                }
                if (t[i] == 'S') t2 += "PS";
            }
            k++;
            t = t2;
        }

        if (st.p == P && st.r == R && st.s == S){
            cout << order(t, n) << endl;
            continue;
        }

        st = (state){0,1,0};
        t = "R";
        k = 0;
        while (st.p + st.r + st.s < n){
            int np = st.p + st.s;
            int nr = st.r + st.p;
            int ns = st.s + st.r;
            st.p = np;
            st.r = nr;
            st.s = ns;
            string t2 = "";
            for(int i = 0; i<t.size(); i++){
                if (t[i] == 'P'){
                    t2 += "PR";

                }
                if (t[i] == 'R'){
                    t2 += "RS";

                }
                if (t[i] == 'S') t2 += "PS";
            }
            t = t2;
            k++;
        }
        if (st.p == P && st.r == R && st.s == S){
            cout << order(t, n) << endl;
            continue;
        }

        st = (state){0,0,1};
        t = "S";
        k = 0;
        while (st.p + st.r + st.s < n){
            int np = st.p + st.s;
            int nr = st.r + st.p;
            int ns = st.s + st.r;
            st.p = np;
            st.r = nr;
            st.s = ns;
            string t2 = "";
            for(int i = 0; i<t.size(); i++){
                if (t[i] == 'P'){
                    t2 += "PR";

                }
                if (t[i] == 'R'){
                    t2 += "RS";

                }
                if (t[i] == 'S') t2 += "PS";
            }
            k++;
            t = t2;
        }
        if (st.p == P && st.r == R && st.s == S){
            cout << order(t, n) << endl;
            continue;
        }

        cout << "IMPOSSIBLE" << endl;


    }


}
