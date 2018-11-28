#include <cstdio>
#include <vector>

using namespace std;

#define rep(i, n) for(int i=0; i<(n); ++i)

int main(){
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; ++t){
        vector<int> row(2);
        vector<vector<vector<int> > > cards(4, vector<vector<int> >(4, vector<int>(2)));
        rep(k, 2){
            scanf("%d", &row[k]);
            rep(i, 4)rep(j, 4)scanf("%d", &cards[i][j][k]);
        }
        vector<int> ans;
        rep(i, 4)rep(j, 4){
            if(cards[row[0]-1][i][0] == cards[row[1]-1][j][1]){
                ans.push_back(cards[row[0]-1][i][0]);
            }
        }
        printf("Case #%d: ", t);
        if(ans.empty())puts("Volunteer cheated!");
        else if(2 <= (int)ans.size())puts("Bad magician!");
        else printf("%d\n", ans[0]);
    }
    return 0;
}
