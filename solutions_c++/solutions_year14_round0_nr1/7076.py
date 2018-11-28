#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int test;
    int a, b;
    vector<int> first[4];
    vector<int> second[4];
    vector<int> v;
    int br;

    scanf("%d", &test);
    for(int t = 0; t < test; ++t) {
        scanf("%d", &a);
        for(int i = 0; i < 4; ++i) {
            first[i].clear();
            for(int j = 0; j < 4; ++j) {
                int br;
                scanf("%d", &br);
                first[i].push_back(br);
            }
        }

        scanf("%d", &b);
        for(int i = 0; i < 4; ++i) {
            second[i].clear();
            for(int j = 0; j < 4; ++j) {
                scanf("%d", &br);
                second[i].push_back(br);
            }
        }        

        --a; --b;
        
        sort(first[a].begin(), first[a].end());
        sort(second[b].begin(), second[b].end());

        v.clear();

        //printf("%d %d %d %d\n", first[a][0], first[a][1], first[a][2], first[a][3]);
        //printf("%d %d %d %d\n", second[b][0], second[b][1], second[b][2], second[b][3]);

        set_intersection(first[a].begin(), first[a].end(), second[b].begin(), second[b].end(), std::back_inserter(v));

        printf("Case #%d: ", t+1);
        if(v.size() == 1) {
            printf("%d", v[0]);
        } else if(v.size() > 1) {
            printf("Bad magician!");
        } else { 
            printf("Volunteer cheated!");
        }
        printf("\n");
    }

    

    return 0;
}
