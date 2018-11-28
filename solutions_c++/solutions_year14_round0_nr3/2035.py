
#include <iostream>
#include <queue>
#include <utility>
#include <cstdio>
using namespace std;

char grid[5][5];


int R,C,M;

void zeroifyGrid(){
    for(int x=0;x<C;x++){
        for(int y=0;y<R;y++){
            if(grid[x][y]=='*')
                continue;
            int count = 0;
            if(x!=0){
                if(grid[x-1][y]=='*')
                    count++;
                if(y!=0){
                    if(grid[x-1][y-1]=='*')
                        count++;
                }
                if(y!=R-1){
                    if(grid[x-1][y+1]=='*')
                        count++;
                }
            }
            if(x!=C-1){
                if(grid[x+1][y]=='*')
                    count++;
                if(y!=R-1){
                    if(grid[x+1][y+1]=='*')
                        count++;
                }
                if(y!=0){
                    if(grid[x+1][y-1]=='*')
                        count++;
                }
            }
            if(y!=0)
                if(grid[x][y-1]=='*')
                    count++;
            if(y!=R-1)
                if(grid[x][y+1]=='*')
                    count++;
            grid[x][y]='0'+count;
        }
    }
}

bool checkGrid(){
    int mineCount = 0;
    for(int x=0;x<C;x++){
        for(int y=0;y<R;y++){
            if(grid[x][y]=='*'){
                mineCount++;
            }
        }
    }

    if(mineCount!=M)
        return false;
    zeroifyGrid();
    queue<pair<int,int> > todo;
    todo.push(make_pair(0,0));
    while(!todo.empty()){
        pair<int,int> curr = todo.front();
        todo.pop();
        int x = curr.first;
        int y = curr.second;
        if(x<0 || y<0 || x>=C || y>=R){
            continue;
        }
        if(grid[x][y]=='*')
            return false;
        if(grid[x][y]=='0'){
            todo.push(make_pair(x-1,y));
            todo.push(make_pair(x-1,y-1));
            todo.push(make_pair(x,y-1));
            todo.push(make_pair(x+1,y-1));
            todo.push(make_pair(x+1,y));
            todo.push(make_pair(x+1,y+1));
            todo.push(make_pair(x,y+1));
            todo.push(make_pair(x-1,y+1));
        }
        grid[x][y]='.';
    }
    for(int x=0;x<C;x++){
        for(int y=0;y<R;y++){
            if(grid[x][y]!='.' && grid[x][y]!='*'){
                return false;
            }
        }
    }
    return true;
}


void makeGrid(int* rows){
    for(int y=0;y<R;y++){
        int x;
        for(x=0;x<rows[y];x++){
            grid[x][y] = '.';
        }
        for(;x<C;x++){
            grid[x][y] = '*';
        }
    }
}

void outputGrid(){
    for(int y=0;y<R;y++){
        for(int x=0;x<C;x++){
            if(x==0 && y==0){
                printf("c");
            }
            else{
                printf("%c",grid[x][y]);
            }
        }
        printf("\n");
    }
}

int main(){
    int nCases;
    cin >> nCases;
    for(int c=1;c<=nCases;c++){
        cin >> R >> C >> M;
        bool hasGrid = false;
        printf("Case #%d:\n",c);
        for(int i1=0;i1<=5;i1++){
            for(int i2=0;i2<=5;i2++){
                for(int i3=0;i3<=5;i3++){
                    for(int i4=0;i4<=5;i4++){
                        for(int i5=0;i5<=5;i5++){
                            int arr[5];
                            arr[0]=i1;
                            arr[1]=i2;
                            arr[2]=i3;
                            arr[3]=i4;
                            arr[4]=i5;
                            makeGrid(arr);
                            if(checkGrid()){
                                outputGrid();
                                //zeroifyGrid();
                                //outputGrid();
                                hasGrid = true;
                                break;
                            }
                        }
                        if(hasGrid)
                            break;
                    }
                    if(hasGrid)
                        break;
                }
                if(hasGrid)
                    break;
            }
            if(hasGrid)
                break;
        }
        if(!hasGrid){
            printf("Impossible\n");
        }
    }
    return 0;
}
