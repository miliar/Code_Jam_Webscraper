/*#include<stdio.h>
int main(){
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++)
            printf("%d ", i * 10 + j + 1);
        printf("\n");
    }
    
    printf("\n\n");
    
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++)
            printf("%d ", i + j * 10 + 1);
        printf("\n");
    }
}*/

#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

int n;
vector<vector<int> > v;
vector<vector<int> > b;
int dx[2] = { 1, 0 };
int dy[2] = { 0, 1 };
bool c[51], done;

bool fill(int at, int index, int dir){
    int x = at;
    int y = 0;
    if(dir == 0) swap(x, y);
    
    bool ret = true;
    for(int i = 0; i < n; i++){
        if(b[y][x] && b[y][x] != v[index][i]){
            ret = false;
            break;
        }
        b[y][x] = v[index][i];
        x += dx[dir];
        y += dy[dir];
    }
    
    return ret;
}

void solve(int index, int row){
    if(index == 2 * n - 1){
        vector<vector<int> > tmp;
        for(int i = 0; i < n; i++)
            tmp.push_back(b[i]);
        for(int j = 0; j < n; j++){
            vector<int> tmp2(n);
            for(int i = 0; i < n; i++)
                tmp2[i] = b[i][j];
            tmp.push_back(tmp2);
        }
        
        sort(tmp.begin(), tmp.end());
        
        int size = tmp.size();
        bool printed = false;
        for(int i = 0; i < size; i++){
            if(i == size - 1 || v[i] != tmp[i]){
                printed = true;
                for(int j = 0; j < n; j++)
                    printf("%d ", tmp[i][j]);
                printf("\n");
                break;
            }
        }
        
        if(printed)
            done = true;
        return;
    }
    
    for(int j = 0; !done && b[0][j] && j < n; j++){
        if(!c[j] && b[0][j] == v[index][0]){
            vector<vector<int> > tmp = b;
            c[j] = true;
            if(fill(j, index, 1))
                solve(index + 1, row);
            b = tmp;
            c[j] = false;
        }
    }
    
    if(!done){
        for(int i = 0; i < n; i++){
            if(!b[i][0] || b[i][0] == v[index][0]){
                vector<vector<int> > tmp = b;
                if(fill(i, index, 0))
                    solve(index + 1, row + 1);
                b = tmp;
                
                break;
            }
        }
    }
}

int main(){
    freopen("/Users/WarYi/Desktop/b.in", "r", stdin);
    freopen("/Users/WarYi/Desktop/b.out", "w", stdout);
    
    int t;
    scanf("%d", &t);
    for(int T = 1; T <= t; T++){
        scanf("%d", &n);
        
        b.resize(n);
        for(int i = 0; i < n; i++)
            b[i].resize(n);
        
        for(int i = 0; i < 2 * n - 1; i++){
            v.push_back(vector<int>());
            for(int j = 0; j < n; j++){
                int tmp;
                scanf("%d", &tmp);
                v[i].push_back(tmp);
            }
        }
        
        sort(v.begin(), v.end());
        
        printf("Case #%d: ", T);
    
        solve(0, 0);
        v.clear();
        b.clear();
        done = false;
        for(int i = 0; i < 51; i++)
            c[i] = false;
    }
    
    return 0;
}