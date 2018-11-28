#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;
int R,C,M;
int dirx[8]={-1,-1,-1,0,0,1,1,1};
int diry[8]={-1,0,1,-1,1,-1,0,1};
int nbrV=0;
bool safe(int x,int y){
    return x>=0 && y>=0 && x<R && y<C;
}

bool mine(int x,int y,vector<string>& grid){
    for(int i=0;i<8;i++){
            if(safe(x+dirx[i],y+diry[i]) && grid[x+dirx[i]][y+diry[i]]=='*')
            return true;
    }
    return false;
}

void DFS(int x,int y,vector<string>& grid,vector<vector<bool> >& visited){
    nbrV++;
    visited[x][y]=true;
    if(mine(x,y,grid)){
            return ;
    }
    for(int i=0;i<8;i++){
            int nx=x+dirx[i];
            int ny=y+diry[i];
            if(safe(nx,ny) && !visited[nx][ny] && grid[nx][ny]!='*')
                DFS(nx,ny,grid,visited);
    }
}

int count(){
    return nbrV;
}

void aff(int x,int y,int z,int w){
    cout<<x<<" "<<y<<" "<<z<<" "<<w<<endl;
}

int main() {
    ifstream cin("C-small.in");
    ofstream cout("C-small.out");
    int t;
    cin>>t;
    int c=0;
    while(t--){
            aff(t,R,C,M);
            c++;
            vector<string> grid;
            bool found=false;
            cin>>R>>C>>M;
            string s(M,'*');
            string s2(R*C-M,'.');
            string all=s+s2;
    do{
                    grid.clear();
                    for(int i=0;i<R;i++){
                            grid.push_back(all.substr(i*C,C));
                    }
                    for(int i=0;i<R && !found;i++)
                        for(int j=0;j<C && !found;j++){
                         vector<vector<bool> > visited(R,vector<bool>(C,false));
                         if(grid[i][j]!='*'){
                            nbrV=0;
                            DFS(i,j,grid,visited);
                            if(count()==R*C-M){
                                grid[i][j]='c';
                                found=true;
                                break;
                            }
                          }
                        }
                }while(next_permutation(all.begin(),all.end()) && !found);
                cout<<"Case #"<<c<<":"<<endl;
                if(found){
                        for(int i=0;i<R;i++)
                            cout<<grid[i]<<endl;
                }
                else{
                        cout<<"Impossible"<<endl;
                }
        }
}
