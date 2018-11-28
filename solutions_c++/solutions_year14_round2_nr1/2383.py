#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
#include <cmath>
#include <cstdlib>
using namespace std;

typedef struct
{
    string os;
    string ss;
    vector<int> count;
}Data;
typedef struct
{
    int min;
    int max;
}Range;

int main(int argc, char **argv)
{
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; cas ++){
        int N;
        cin >> N;
        vector<Data> ds(N);
        for(int i = 0; i < N; i++){
            cin >> ds[i].os;
            char last;
            last = ds[i].os[0];
            int n = 0;
            for(int j = 0; j <ds[i].os.size(); j++){
                if(last == ds[i].os[j]){
                    n++;
                }else{
                    ds[i].count.push_back(n);
                    ds[i].ss += last;
                    last = ds[i].os[j];
                    n = 1;
                }
            }
            ds[i].count.push_back(n);
            ds[i].ss += last;

        }
        string s = ds[0].ss;
        bool won = false;
        for(int i = 1; i < N; i++){
            if(ds[i].ss != s) {
                won = true;
                break;
            }
        }
        cout << "Case #" << cas << ": "; 
        if(won){
            cout << "Fegla Won" << endl;
            continue;
        }
        int m = ds[0].count.size();
        vector<Range> rs;
        for(int k = 0; k < m; k++){
            Range r;
            r.min = 100;
            r.max = 0;
            for(int i = 0; i < N; i++){
                if(ds[i].count[k] < r.min){
                    r.min = ds[i].count[k];
                }
                if(ds[i].count[k] > r.max){
                    r.max = ds[i].count[k];
                }
            }
            rs.push_back(r);
        }
        int sum = 0;
        for(int k = 0; k < m; k++){
            int actionsMin = 100;
            for(int l = rs[k].min; l <= rs[k].max; l++){ 
                int actions = 0;
                for(int j = 0; j < N; j++){
                    actions += abs(ds[j].count[k] - l);
                }
                if(actions < actionsMin){
                    actionsMin = actions;
                }
            }
            sum += actionsMin;
        }
        cout << sum << endl;

    }
    return 0;
}
