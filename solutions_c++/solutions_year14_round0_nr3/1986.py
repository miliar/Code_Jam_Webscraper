#include <cstdio>
#include <iostream>
#include <cstdlib>

using namespace std;

int width;
int height;
int m_map[60][60];
bool traveled[60][60];
bool find_ans;

int dirx[] = {-1,-1,0,1,1,1,0,-1};
int diry[] = {0,1,1,1,0,-1,-1,-1};

bool in_range(int x, int y){
    if (x>0 && y>0 && x<=height && y<=width)
        return true;
    else
        return false;
}

bool check_alive(int x, int y, int temp_map[][60]){
    bool is_dead = true;
    if (!in_range(x,y)) return false;
    if (temp_map[x][y] == 0) return true;
    for (int k=0; k<8; k++){
        int x1 = x + dirx[k];
        int y1 = y + diry[k];
        if (in_range(x1,y1) && (temp_map[x1][y1]==0)){
            is_dead = false;
            break;
        }
    }
    return !is_dead;
}

int nextx(int x, int y){
    if (y==width)
        return x+1;
    else
        return x;
}

int nexty(int x, int y){
    if (y==width)
        return 1;
    else
        return y+1;
}

int assign_value(int x, int y){
    if (m_map[x][y] == 1)
        return 2;
    for (int k=0; k<8; k++){
        int x1 = x + dirx[k];
        int y1 = y + diry[k];
        if (m_map[x1][y1] == 1)
            return 1;
    }
    return 0;
}
void print_map(int temp_map[][60]){
    for (int i=1; i<=height; i++){
        for (int j=1; j<=width; j++)
            cout << temp_map[i][j];
        cout << endl;
    }
}

void flood_fill(int x, int y, int temp_map[][60]){
    traveled[x][y] = true;
    if (temp_map[x][y] != 0) return;
    for (int k=0; k<8; k++){
        int x1 = x + dirx[k];
        int y1 = y + diry[k];
        if (in_range(x1,y1) && temp_map[x1][y1] != 2 && !traveled[x1][y1]){
            flood_fill(x1,y1, temp_map);
        }
    }
}

bool check_map(){
    int new_map[60][60];
    for (int i=1; i<=height; i++)
        for (int j=1; j<=width; j++)
            new_map[i][j] = assign_value(i,j);
    bool is_ans = true;
    int mine_count = 0;
    for (int i=1; i<=height; i++)
        for (int j=1; j<=width; j++)
            if (new_map[i][j] == 2) mine_count += 1;
    if (mine_count == height * width - 1)
        return true;

    for (int i=1; i<=height; i++)
        for (int j=1; j<=width; j++)
            traveled[i][j] = false;

    bool flag = false;
    int countt = 0;
    for (int i=1; i<=height; i++){
        if (flag) break;
        for (int j=1; j<=width; j++)
        if (new_map[i][j] == 0){
            flood_fill(i,j, new_map);
            flag = true;
            countt += 1;
            break;
        }
    }
    /*
    print_map(new_map);
    cout << "ans?" << is_ans  << endl;
    cout << countt << endl << endl << endl;
    */
    for (int i=1; i<=height; i++)
        for (int j=1; j<=width; j++)
        if (new_map[i][j] != 2 && !traveled[i][j]){
            is_ans = false;
        }

    return is_ans;
}

void m_search(int x, int y, int left){
    if (find_ans) return;
    if (left == 0){
        if (check_map()){
            find_ans = true;
        }
        return;
    }
    if (!in_range(x,y)) return;
    for (int choice =0; choice<=1; choice++){
        m_map[x][y] = choice;
        int x1 = nextx(x,y);
        int y1 = nexty(x,y);
        m_search(x1,y1,left-choice);
        if (find_ans) break;
        m_map[x][y] = 0;
    }
}

int main(){
    freopen("t.in","r",stdin);
    freopen("t.out","w",stdout);
    int tests;
    cin >> tests ;
    for (int test=1; test<=tests; test++){
        int remains = 0;
        cin >> height >> width >> remains;
        for (int i=0; i<=height+1; i++)
            for (int j=0; j<=width+1; j++)
                m_map[i][j] = 0;
        find_ans = false;
        m_search(1,1,remains);
        cout << "Case #" << test << ":" << endl;
        if (find_ans){
            bool put_c = false;

            for (int i=1; i<=height; i++)
                for (int j=1; j<=width; j++)
                    if (m_map[i][j] == 0 && !put_c){
                        m_map[i][j] = -1;
                        put_c = true;
                    }
            for (int i=1; i<=height; i++){
                for (int j=1; j<=width; j++)
                    if (m_map[i][j] == 0)
                        cout << ".";
                    else if (m_map[i][j] == -1)
                        cout << "c";
                    else
                        cout << "*";
                cout << endl;
            }
        } else {
            cout << "Impossible" << endl;
        }
    }
}
