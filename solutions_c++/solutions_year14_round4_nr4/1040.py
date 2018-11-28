#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <map>
#include <string>

using namespace std;

int res, res_cnt, n, m;
string s[22];
map<string, int> mm[6];
int flag[22];

void update(){
    for (int i = 1; i <= n; i++) mm[i].clear();

    for (int i = 0; i < m; i++){
        string ss = "";
        mm[flag[i]][ss] = 1;
        //cout << flag[i] << " ";

        for (int j = 0; j < s[i].length(); j++){
            ss = ss + s[i][j];
            mm[flag[i]][ss] = 1;
        }
    }
    //cout << endl;

    int cnt = 0;
    for (int i = 1; i <= n; i++){
        if (mm[i].size() == 0) return ;

        cnt += mm[i].size();
    }

    if (cnt > res){
        res = cnt;
        res_cnt = 0;
    }

    if (cnt == res) res_cnt++;
}

void attempt(int step){
    if (step == m){
        update();
        return ;
    }

    for (int i = 1; i <= n; i++){
        flag[step] = i;

        attempt(step + 1);
    }
}

int main(){
    ifstream input ("D-small-attempt0.in");
    ofstream output ("output.txt");

    int T;
    input >> T;

    for (int t = 1; t <= T; t++){
        res = -1;

        input >> m >> n;
        input.ignore(255, '\n');

        for (int i = 0; i < m; i++)
            input >> s[i];

        attempt(0);

        output << "Case #" << t << ": " << res << " " << res_cnt;
        cout << t << endl;
        if (t != T) output << endl;
    }

    input.close();
    output.close();

    return 0;
}


