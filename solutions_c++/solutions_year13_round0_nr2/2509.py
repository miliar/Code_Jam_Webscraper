#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int n, m, t;
vector<vector<int> > a;


bool arImanoma();
void printMatrix();
pair<int, int> getMaximum();


int main(){
    freopen("B-large.in", "r", stdin);
    freopen("solution.txt", "w", stdout);
    scanf("%d", &t);

    for(int i = 0; i < t; ++i){
        cin >> n >> m;
        a.clear();
        a.resize(n, vector<int>(m));


        for(int j = 0; j < n; ++j)
            for(int u = 0; u < m; ++u)
                scanf("%d", &a[j][u]);

        if(arImanoma())
            printf("Case #%d: YES\n", i+1);
        else
            printf("Case #%d: NO\n", i+1);

    }
}

bool arImanoma(){
while(!a.empty()){
    pair<int, int> c = getMaximum();
    //cout << c.first << " " << c.second << endl;
    //printMatrix();
    //getch();
    if(c.first == -1)
        break;


    int min = a[c.first][c.second], my = 0, mx = 0;

    for(int i = 0; i < a.size(); ++i)
        if(a[i][c.second] == min)
            ++my;

    for(int i = 0; i < a[0].size(); ++i)
        if(a[c.first][i] == min)
            ++mx;


    bool px = (mx != a[0].size()), py = (my != a.size());

    if(px & py)
        return false;

    if(!px)
        a.erase(a.begin() + c.first);

    else
        for(int i = 0; i < a.size(); ++i){
            a[i].erase(a[i].begin() + c.second);
            if(a[i].empty())
                a.erase(a.begin() + i);
        }
}
return true;
}

void printMatrix(){
    for(int i = 0; i < a.size(); ++i){
        for(int j = 0; j < a[i].size(); ++j)
                printf("%d", a[i][j]);
    printf("\n");
    }

}

pair<int, int> getMaximum(){
    int min = 99898978;
    pair<int, int> c = make_pair(-1,-1);

    for(int i = 0; i < a.size(); ++i)
        for(int j = 0; j < a[i].size(); ++j)
            if(min > a[i][j]){
                c = make_pair(i, j);
                min = a[i][j];
            }

    return c;
}
