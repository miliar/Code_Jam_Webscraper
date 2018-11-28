#include <map>
#include <vector>
#include <iostream>

using namespace std;
typedef long long LL;

LL fee(LL dist, int N){
    return dist * N - dist*(dist-1)/2;
}

LL solve(map<int,int>& move, int N){
    map<int,int>::iterator it = move.begin();
    LL res = 0;
    for(; it != move.end(); it++){
        if(it->second > 0) continue;
        int v = -it->second;
        map<int,int>::iterator it2 = it;
        while(v > 0){
            it2--;
            if(it2->second < 0) continue;
            int red = min(v, it2->second);
            it2->second -= red;
            v -= red;
            LL dist = it->first - it2->first;
            res += fee(dist, N) * red;
            if(v > 0 && it2 == move.begin()){
                cerr << "error" << endl;
                return -1;
            }
        }
    }
    return res;
}


int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        int N, M;
        cin >> N >> M;
        map<int, int> move;
        LL normal = 0;
        for(int m = 0; m < M; m++){
            int start, end, num;
            cin >> start >> end >> num;
            move[start] += num;
            move[end] -= num;
            LL dist = end - start;
            normal += fee(dist, N) * num;
        }
        LL res = solve(move, N);
        cout << "Case #" << t << ": " << (normal-res) << endl;
    }
    return 0;
}

