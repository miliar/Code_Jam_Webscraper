/*#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

multiset<int> :: iterator it;
multiset<int> que;

int main()
{
    int n;
    cin >> n;
    while(n--){
        int k;
        cin >> k;
        que.insert(k);
        it = que.find(k);
        if(que.size() > 1){
            if(it != que.end()){
                it++;
                cout << *it << "----";
                it--;
                cout << *it << endl;
            }
        }
    }
    it = que.begin();
    while(it != que.end()){
        cout << *it << endl;
        it++;
    }
    return 0;
}
*/
/*
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <set>
#include <stack>
#include <cstring>

using namespace std;

stack<int> st;
multiset<int> tab;
multiset<int> :: iterator it;
char mod[3][20] = {"Push","Pop","PeekMedian"};

int main()
{
    int n, k;
    char s[20];
    scanf("%d", &n);
    while(n--){
        scanf("%s",s);
        if(strcmp(s, mod[0]) == 0){
            scanf("%d", &k);
            st.push(k);
            tab.insert(k);
            if(tab.size() == 1)it = tab.begin();
            else if(tab.size() % 2){
                if(k <= )
            }
        }
        else if(strcmp(s, mod[1]) == 0){

        }
        else {

        }
    }
    return 0;
}*/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define ma 5

int dir[4][2] = {{0, 1}, {1, 0}, {1, 1}, {1, -1}};
char maze[ma][ma];

int dfs(int x, int y, int c, int len, int k){
    if(len == 4)return 1;
    else if(k == 1 && len == 3)return 1;
    if(x +dir[c][0] < 4 && y + dir[c][1] < 4){
        if(maze[x +dir[c][0]][y + dir[c][1]] == maze[x][y]){
            if(dfs(x +dir[c][0], y + dir[c][1], c, len + 1, k))return 1;
        }
        else if(maze[x +dir[c][0]][y + dir[c][1]] == 'T' && k == 0){
            if(dfs(x +dir[c][0], y + dir[c][1], c, len, k + 1))return 1;
        }
    }
    return 0;
}

int main()
{
    freopen("A-small-attempt6.in","r",stdin);
    freopen("A-small-attempt6.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int ca = 1; ca <= t;ca++){
        getchar();
        printf("Case #%d: ",ca);
        for(int i = 0; i < 4; i++){
            scanf("%s",maze[i]);
        }
        int tag = 0;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                for(int k = 0; k < 4; k++){
                    if(maze[i][j] == 'X' || maze[i][j] == 'O'){
                        if(dfs(i, j, k, 1, 0)){
                            tag = 1;
                            if(maze[i][j] == 'X')puts("X won");
                            else puts("O won");
                            //cout << i << ' ' << j << ' ' << k << endl;
                            break;
                        }
                    }
                    else if(maze[i][j] == 'T'){
                        if(dfs(i, j, k, 0, 1)){
                            tag = 1;
                            if(maze[i + dir[k][0]][j + dir[k][1]] == 'X')puts("X won");
                            else puts("O won");
                            //cout << i << ' ' << j << ' ' << maze[i][j] << endl;
                            break;
                        }
                    }
                }
                if(tag)break;
            }
            if(tag)break;
        }
        if(tag == 0){
            for(int i = 0; i < 4; i++){
                for(int j = 0; j < 4; j++){
                    if(maze[i][j] == '.'){
                        puts("Game has not completed");
                        tag = 1;
                        break;
                    }
                }
                if(tag)break;
            }
            if(tag == 0)puts("Draw");
        }
    }
    return 0;
}
