#include <iostream>
#include <vector>
#include <map>

int desired[101][101];
int heights[101][101];

std::multimap<int, std::pair<int, int> > locs;

int W, H;

bool do_search() {
    for(std::multimap<int, std::pair<int, int> >::reverse_iterator ri = locs.rbegin();
        ri != locs.rend(); ++ri) {

        std::pair<int, int> l = ri->second;
        
        // horizontal sweep
        bool works = true;
        for(int i = 0; i < W; i ++) {
            if(desired[i][l.second] > ri->first) { works = false; break; }
        }
        if(works) {
            for(int i = 0; i < W; i++) {
                heights[i][l.second] = ri->first;
            }
            continue;
        }

        works = true;
        for(int i = 0; i < H; i ++) {
            if(desired[l.first][i] > ri->first) { works = false; break; }
        }
        if(works) {
            for(int i = 0; i < H; i++) {
                heights[l.first][i] = ri->first;
            }
            continue;
        }

        return false;
    }
    return true;
}

int main() {
    int T;
    std::cin >> T;
    for(int C = 0; C < T; C ++) {
        locs.clear();
        std::cin >> H >> W;

        /*for(int j = 0; j < N; j ++) {
            for(int i = 0; i < M; i ++) {
                std::cin >> desired[i][j];
                locs.insert(std::make_pair(desired[i][j], std::make_pair(i, j)));
                heights[i][j] = 100;
            }
        }*/

        for(int y = 0; y < H; y ++) {
            for(int x = 0; x < W; x ++) {
                std::cin >> desired[x][y];
                locs.insert(std::make_pair(desired[x][y], std::make_pair(x, y)));
                heights[x][y] = 100;
            }
        }

        if(do_search()) std::cout << "Case #" << C+1 << ": YES" << std::endl;
        else std::cout << "Case #" << C+1 << ": NO" << std::endl;
    }
    return 0;
}
