#include <iostream>
#include <queue>

#define INF 1<<30

int N, K;

int visited[1<<20];

int keys[20][200], req[20];
int starting[200];

int left(int mask, int key) {
    int count = starting[key];

    for(int i = 0; i < N; i ++) {
        if((mask & (1<<i)) == 0) continue;

        if(req[i] == key) {
            count --;
        }
        count += keys[i][key];
    }

    return count;
}

/*int dp(int mask) {
    if(visited[mask] != INF) return visited[mask];
    if(mask == 0) return -1;

    // try adding each one in turn
    for(int i = 31; i >= 0; i --) {
        int m = 1<<i;
        if((mask & m) == 0) continue;

        int p = dp(mask & ~m);
        if(p == INF) continue;

        visited[mask] = mask & ~m;
        return visited[mask];
    }

    return INF;
}*/

void search() {
    std::queue<std::pair<int, int> > q;
    q.push(std::make_pair(0, 0));
    while(q.size() > 0) {
        std::pair<int, int> p = q.front();
        q.pop();
        int n = p.first;
        if(visited[n] != INF) continue;
        visited[n] = p.second;
        //std::cout << "@ " << p.first << std::endl;

        for(int i = 0; i < N; i ++) {
            int mask = 1<<i;
            if((n & mask) == 1) continue;
            //std::cout << "passed mask check " << std::endl;

            //std::cout << "left(" << n << ", " << req[i] << "): " << left(n, req[i]) << std::endl;
            if(left(n, req[i]) == 0) continue;

            q.push(std::make_pair(n | mask, n));
        }
    }
}

int main() {
    int T;
    std::cin >> T;
    for(int C = 0; C < T; C ++) {
        for(int i = 0; i < 200; i ++) starting[i] = 0;
        for(int i = 0; i < 20; i ++) for(int j = 0; j < 200; j ++)
            keys[i][j] = 0;

        std::cin >> K >> N;
        //std::cout << "K: " << K << std::endl;
        for(int i = 0; i < 1<<N; i ++) visited[i] = INF;

        for(int i = 0; i < K; i ++) {
            int v;
            std::cin >> v;
            //std::cout << "Starting with a " << v-1 << std::endl;
            starting[v-1]++;
        }

        for(int i = 0; i < N; i ++) {
            std::cin >> req[i];
            req[i] --;
            int count;
            std::cin >> count;
            for(int j = 0; j < count; j ++) {
                int type;
                std::cin >> type;
                keys[i][type-1] ++;
            }
        }

        //int v = dp((1<<N) - 1);
        search();
        int v = visited[(1<<N) - 1];
        std::cout << "Case #" << C+1 << ":";
        if(v == INF) std::cout << " IMPOSSIBLE" << std::endl;
        else {
            std::vector<int> selected;
            int cursor = (1<<N) - 1;
            while(cursor != -1 && cursor != 0) {
                selected.push_back(cursor);
                cursor = visited[cursor];
            }
            selected.push_back(0);
            for(int i = selected.size()-1; i >= 1; i --) {
                //std::cout << "\t" << (selected[i-1] ^ selected[i]) << std::endl;
                for(int j = 0; j < N; j ++) {
                    if((1 << j) == (selected[i-1] ^ selected[i])) {
                        std::cout << " " << j+1;
                        break;
                    }
                }
            }
            std::cout << std::endl;
            //std::cout << "possible" << std::endl;
        }
    }
    return 0;
}
