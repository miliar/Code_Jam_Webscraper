#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int dx[]={-1,0,1,0}, dy[]={0,1,0,-1};

int revDir(int dir)
{
    switch(dir) {
        case 0:
            return 2;
        case 1:
            return 3;
        case 2:
            return 0;
        case 3:
            return 1;
        default:
            return -1;
    }
}

int mapToDir(int ch)
{
    switch(ch) {
        case '<':
            return 3;
        case '>':
            return 1;
        case '^':
            return 0;
        case 'v':
            return 2;
        default:
            return -1;
    }
}

int dirToMap(int dir)
{
    switch(dir) {
        case 0:
            return '^';
        case 1:
            return '>';
        case 2:
            return 'v';
        case 3:
            return '<';
        default:
            return '!';
    }
}

bool check(int x, int y, vector<string> &map)
{
    return x>=0 && y>=0 && x<(int)map.size() && y<(int)map[0].size();
}

bool checkDir(int x, int y, int dir, vector<string> &map)
{
    int nx=x+dx[dir], ny=y+dy[dir];
    while(check(nx, ny, map) && map[nx][ny]=='.') {
        nx += dx[dir]; ny += dy[dir];
    }
    if(check(nx,ny,map)) return true;
    return false;
}

bool checkRound(int x, int y, vector<string> &map)
{
    for(int i=0; i<4; i++) {
        if(checkDir(x,y,i,map)) return true;
    }
    return false;
}

void run(int x, int y, vector<string> &map, int &cnt, int &rest)
{
    if(checkDir(x,y, mapToDir(map[x][y]), map)) return;
    if(checkRound(x,y,map)) {
        cnt++;
    } else {
        rest++;
    }
}

int main()
{
    int T, Tcnt=1;
    cin>>T;
    for(; T; T--,Tcnt++) {
        int R, C;
        cin>>R>>C;
        vector<string> map;
        map.resize(R);
        for(int i=0; i<R; i++) {
            cin>>map[i];
        }
        int cnt=0;
        int rest=0;
        for(int i=0; i<R; i++) {
            for(int j=0; j<C; j++) {
                if(map[i][j]=='.') continue;
                run(i,j,map,cnt,rest);
            }
        }
        cout<<"Case #"<<Tcnt<<": ";
        if(rest) {
            cout<<"IMPOSSIBLE"<<endl;
        } else {
            cout<<cnt<<endl;
        }
    }
    return 0;
}

