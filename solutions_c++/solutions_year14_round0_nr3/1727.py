#include <stdio.h>
#include <memory.h>
#include <set>
#include <vector>
using namespace std;
#define MAX 100
set<int> search_set;
int R = 0,C = 0,M = 0;
int sr = 0, sc = 0;
int arr[MAX][MAX];
bool solved = false;
inline bool in_set(int num) {
    return search_set.find(num) != search_set.end();
}
inline int is_neighbor(int r, int c, int i, int j) {
    return (r - i) * (r - i) <= 1 && (c - j) * (c - j) <= 1;
}
inline int parse_int() {
    int sum = 0;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            sum <<= 1;
            sum += (arr[i][j] == 1);
        }
    }
    return sum;
}
void print_map() {
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (i == sr && j == sc)
                printf("c");
            else if (!arr[i][j])
                printf("*");
            else
                printf(".");
        }
        printf("\n");
    }
}
int solve(int r, int c, int cnt) {
    //printf("%d %d %d\n",r,c,cnt);
    vector< pair<int,int> >   vec;
    int sum = (arr[r][c] == 0);
    arr[r][c] = 1;
    int feature = parse_int();
    if (solved || cnt + sum > M || in_set(feature)) {
        return 0;
    }
    if (cnt + sum == M) {
        //printf("%d %d\n",sr,sc);
        solved = true;
        print_map();
        return 0;
    }
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (is_neighbor(r,c,i,j) && !arr[i][j]) {
                vec.push_back(make_pair(i,j));
                arr[i][j] = 2;
                sum++;
            }
        }
    }
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (arr[i][j] == 2) {
                solve(i, j, cnt + sum);
            }
        }
    }
    for (int i = 0 ; i < vec.size() ; i++) {
        pair<int,int> pr = vec[i];
        arr[pr.first][pr.second] = 0;
    }
    search_set.insert(feature);
    arr[r][c] = 0;
    //printf("%d %d %d %d\n",r,c,arr[0][0],cnt);
    return 0;
}
int main() {
    int tt = 0;
    scanf("%d",&tt);
    for (int t = 0; t < tt; t++) {
        solved = false;
        search_set.clear();
        memset(arr,0,sizeof(arr));
        scanf("%d%d%d",&R,&C,&M);
        M = R * C - M;
        //printf("%d %d %d\n",R,C,M);
        printf("Case #%d:\n",t + 1);
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                sr = i;
                sc = j;
                solve(i,j,0);

            }
        }
        if (!solved)
            printf("Impossible\n");
    }
    return 0;
}
