#include<iostream>
#include<cstring>
#include<cstdio>
#include<utility>
#include<algorithm>

using namespace std;

pair<int,int> urut[10005];
int tinggi[105][105],row,col,kasus;
bool aman[105][105];

bool cf(const pair<int,int> &a, const pair<int,int> &b) {
    if (tinggi[a.first][a.second] != tinggi[b.first][b.second]) return tinggi[a.first][a.second] < tinggi[b.first][b.second];
    return (a < b);
}

int main() {
    scanf("%d",&kasus);
    for (int l=1;l<=kasus;++l) {
        scanf("%d %d",&row,&col);
        for (int i=0;i<row;++i){
            for (int j=0;j<col;++j) {
                scanf("%d",&tinggi[i][j]);
                aman[i][j] = false;
                urut[i*col+j] = make_pair(i,j);
            }
        }
        sort(urut,urut+row*col,cf);
        
        bool flag = true;
        for (int i=0;i<row*col&&flag;++i) {
            if (aman[urut[i].first][urut[i].second]) continue;
            int y = urut[i].first;
            int x = urut[i].second;
            
            bool ok = true;
            for (int j=0;j<col;++j) {
                if (!aman[y][j] && tinggi[y][j] > tinggi[y][x]) {
                    ok = false;
                    break;
                }
            }
            
            if (ok) {
                for (int j=0;j<col;++j) {
                    aman[y][j] = true;
                }
            }
            
            ok = true;
            for (int j=0;j<row;++j) {
                if (!aman[j][x] && tinggi[j][x] > tinggi[y][x]) {
                    ok = false;
                    break;
                }
            }
            
            if (ok) {
                for (int j=0;j<row;++j) {
                    aman[j][x] = true;
                }
            }
            
            if (!aman[y][x]) flag = false;
        }
        
        printf("Case #%d: ",l);
        if (flag) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
