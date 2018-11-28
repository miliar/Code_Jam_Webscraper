#include<cstdio>
#include<iostream>
#include<string>

using namespace std;

int T, S, num;
bool* cakes;

bool check(){
    for (int i = 0; i < num; ++i){
        if (cakes[i] == false) return false;
    }
    return true;
}


int main(){
    freopen("large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    scanf("%d\n", &T);
    for (int t = 1; t <= T; ++t){
        string line;
        getline(cin, line);
        num = line.length();
        cakes = new bool[num];
        for (int i = 0; i < num; ++i){
            if (line[i] == '+') cakes[i] = true;
            else cakes[i] = false;
        }
        int cnt = 0;
        while (!check()){
            int localcnt = 0;
            while (!cakes[localcnt] && localcnt < num) ++localcnt;
            for (int i = 0; i < localcnt; i++){
                cakes[i] = true;
            }
            if (!localcnt){
                while (cakes[localcnt]){
                    cakes[localcnt++] = false;
                }

            }
            ++cnt;
        }


        printf("Case #%d: %d\n", t, cnt);
        delete [] cakes;
    }
}
