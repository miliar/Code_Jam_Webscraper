#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

int main(){
    int T, N;
    scanf("%d", &T);
    string str;
    for(int i = 1; i <= T; i++){
        printf("Case #%d: ", i);
        scanf("%d", &N);
        vector<string> in;
        for(int j = 0; j < N; j++){
            cin >> str;
            in.push_back(str);
        }
        vector<int> pos(N, 0);
        bool flg = 0;
        int sum, out = 0;
        while(pos[0] != in[0].size()){
            char curChar = in[0][pos[0]];
            vector<int> cnt(N, 0);
            for(int j = 0; j < N; j++){
                while(in[j][pos[j]] == curChar && pos[j] < in[j].size()){
                    cnt[j]++;
                    pos[j]++;
                }
                if(cnt[j] == 0){
                    printf("Fegla Won\n");
                    flg = 1; 
                    break;
                }
            }
            if(flg)
                break;
            sum = 0;
            for(int j = 0; j < N; j++){
                sum += cnt[j];
            }
            int mid = sum/N, mid1 = mid+ 1;
            int change = 0, change1 = 0;
            for(int j = 0; j < N; j++){
                change += abs(cnt[j] - mid);
                change1 += abs(cnt[j] - mid1);
            }
            change = change>change1?change1:change;
            out +=change;
        }
        if(flg)
           continue;
        for(int j = 0; j < N; j++){
            if(pos[j] != in[j].size()){
                printf("Fegla Won\n");
                flg = 1;
            }
        }
        if(flg)
            continue;
        printf("%d\n", out);
        in.clear();
    }
}
