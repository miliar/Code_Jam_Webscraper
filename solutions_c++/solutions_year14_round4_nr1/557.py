#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(vector<int>& files, int cap){
    sort(files.begin(), files.end());
    int res = 0;
    int cur = 0;
    for(int i = files.size()-1; i >= 0; i--){
        if(cur > i) break;
        if(cur == i){
            res++;
            break;
        }
        if(files[cur] + files[i] > cap){
            res++;
        }else{
            cur++;
            res++;
        }
    }
    return res;
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int N, X;
        cin >> N >> X;
        vector<int> files(N);
        for(int i = 0; i < N; i++){
            cin >> files[i];
        }
        int res = solve(files, X);
        cout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}

