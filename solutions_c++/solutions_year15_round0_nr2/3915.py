#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main(){
    freopen("./input.txt", "r", stdin);
//    freopen("./output.txt", "w", stdout);
    int T;
    cin >> T;

    for(int test=0; test<T; test++){
        int D;
        scanf("%d", &D);
        vector<int> data;
        for(int i=0; i<D; i++){
            int elem;
            scanf("%d", &elem);
            data.push_back(elem);
        }
        sort(data.begin(), data.end());

        int res = 0;
        while(true){

            int max_cnt = 0, sz = data.size();
            int i = sz - 1;
            while(i>=0 && data[i] == data[sz-1]) {
                    max_cnt++;
                    i--;
            }

            int second_max = 0;
            if(i>=0) second_max = data[i];

            int move_val = second_max == 0 ? data[sz-1]/2 : data[sz-1]-second_max;
            int level_reduce = second_max == 0 ? move_val : data[sz-1]-max(move_val, second_max);

            if(move_val > second_max){
                move_val = data[sz-1]/2;
                level_reduce = move_val;
            }
//            cout << move_val << endl;
//            for(int i=0; i<sz; i++) cout << data[i] << " ";
//            cout << endl;

            if(max_cnt <= level_reduce){
                for(int i=0; i<max_cnt; i++){
                    data[sz-1-i] -= move_val;
                }
                data.insert(lower_bound(data.begin(), data.end(), move_val), max_cnt, move_val);
                res += max_cnt;
            }
            else{
                break;
            }
        }
        res += data[data.size()-1];
        cout << "Case #" << test+1 << ": " << res;
        if(test < T-1) cout << endl;
    }
    return 0;
}
