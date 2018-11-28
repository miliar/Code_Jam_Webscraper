#include <bits/stdc++.h>

using namespace std;

int main(){ freopen("dat.txt","r",stdin);
            freopen("dat2.txt","w",stdout);
    ios_base::sync_with_stdio(0);
    //cin.tie(0);

    int TC; cin >> TC;

    for(int tc=1;tc<=TC;tc++){
        int x,r,c; cin >> x >> r >> c;
        cout << "Case #" << tc;
        if(r > c) swap(r,c);
        if(x==1) cout << ": GABRIEL\n";
        else if(x==2)
        cout << ((r*c)%2 == 0 ? ": GABRIEL\n" : ": RICHARD\n");
        else if(x == 3){
            if((r*c)%3 == 0 && r != 1)
                cout << ": GABRIEL\n";
            else cout << ": RICHARD\n";
        }
        else if(x==4){
            if((r==3 && c==4) || (r==4 && c==r))
                cout << ": GABRIEL\n";
            else cout << ": RICHARD\n";
        }
    }
}

/*
map<vector<int>, int> m;
map<vector<int>, int>::iterator it;

int solve(vector<int> v) {
    int mx = 0;
    for (int i = 0; i < v.size(); i++) {
        if (v[i] > v[mx]) {
            mx = i;
        }
    }
    if (v[mx] == 1) {
        return 1;
    }
    int res = v[mx];
    vector<int> vv;
    for (int i = 0; i < v.size(); i++) {
        if (v[i] > 1) {
            vv.push_back(v[i] - 1);
        }
    }
    int tmp = 1 + solve(vv);
    if (tmp < res) {
        res = tmp;
    }
    for ()
}

int t, n;
vector<int> v;

int cas = 1;

int main() {
    ios::sync_with_stdio(false);
    //cin.tie(false);
    freopen("dat.txt", "r", stdin);
    cin >> t;
    while (t--) {
        cin >> n;
        v.resize(n);
        for (int i = 0; i < n; i++) {
            cin >> v[i];
        }
        cout << "Case #" << cas++ << ": " << solve(v) << "\n";
    }
}

/*

bool igual(int *a,int *b){
    for(int i=1;i<=9;i++)
        if(a[i] != b[i]) return false;
    return true;
}

struct est{
    int arr[10];
    est(){
        for(int i=0;i<=9;i++) arr[i] = 0;
    }

    bool operator < (const est &o) const{
        for(int i=1;i<=9;i++)
            if(arr[i] != o.arr[i]) return arr[i] < o.arr[i];
        return false;
    }
};

const int MAXN = 100000;
set<est> dic;
est cola[MAXN];
est fin;

bool move(est x, int &enq, int &deq){
    //cout << "entro\n";

    est y;
    for(int i=1;i<=8;i++)
        y.arr[i] = x.arr[i+1];

    if(dic.find(y) == dic.end()){
        dic.insert(y);
        cola[enq++] = y;
    }

    if(igual(y.arr, fin.arr)) return true;

    for(int i=1;i<=9;i++)
        y.arr[i] = x.arr[i];


    for(int i=1;i<=9;i++){
        if(y.arr[i] > 0){
            y.arr[i]--;
            for(int j=1;j<i;j++){//cant a quitar
                y.arr[i-j]++;

                y.arr[j]++;
                if(dic.find(y) == dic.end()){
                    dic.insert(y);
                    cola[enq++] = y;
                }
                if(igual(y.arr, fin.arr)) return true;
                y.arr[j]--;

                for(int k = 1;k<=i && k+j <= 9; k++){
                    if(y.arr[k] > 0){
                        y.arr[k]--;
                        y.arr[k+j]++;
                        if(dic.find(y) == dic.end()){
                            dic.insert(y);
                            cola[enq++] = y;
                        }
                        if(igual(y.arr, fin.arr)) return true;
                        y.arr[k]++;
                        y.arr[k+j]--;
                    }
                }
                y.arr[i-j]--;
            }
            y.arr[i]++;
        }
    }

    //cout << "salio\n";

    return false;
}

int main(){
    ios_base::sync_with_stdio(0);
    //cin.tie(0);
    freopen("dat.txt","r",stdin);

    int TC; cin >> TC;
    for(int tc=1;tc<=TC;tc++){
        int n,x; cin >> n;

        est ini;
        for(int i=1;i<=n;i++){
            cin >> x;
            ini.arr[x]++;
            //cout << "k" << '\n';
        }

        int enq=0,deq=0;
        dic.clear();

        dic.insert(ini);
        cola[enq++] = ini;

        int time = 0;

        bool go = true;
        while(go){
            time++;

            int siz = enq-deq;
            est x;
            for(int i=0;go && i<siz;i++){
                //cout << "--OOO--\n";
                x = cola[deq++];

                //for(int j=1;j<=9;j++) cout << x.arr[j] << ' ';
                //cout << '\n';

                if(move(x, enq, deq)){
                    cout << "Case #" << tc << ": " << time << '\n';
                    go = false;
                }
                //cout << "------\n";
            }
            //cout << "time == " << time << '\n';
        }
    }
}
*/
