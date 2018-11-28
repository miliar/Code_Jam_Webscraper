#include <iostream>
#include <fstream>

using namespace std;

int main(void){
    ifstream fin("lawnmower2.in");
    ofstream fout("lawnmower-out.txt");
    int T;
    fin>>T;

    int grid[11][11];

    for(int t=1;t<=T;t++){

        int n,m;
        fin>>n>>m;

        int i,j;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                fin>>grid[i][j];
            }
        }
        bool check = true;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                if(grid[i][j]==1){
                    bool l,r,d,u;
                    l=r=d=u= true;
                    int x,y;
                    for(x=i,y=j;x<n;x++){
                        if(grid[x][y]==2)r=false;
                    }
                    for(x=i,y=j;x>=0;x--){
                        if(grid[x][y]==2)l=false;
                    }
                    for(x=i,y=j;y<m;y++){
                        if(grid[x][y]==2)d=false;
                    }
                    for(x=i,y=j;y>=0;y--){
                        if(grid[x][y]==2)u=false;
                    }
                    if(!((r&&l)||(d&&u)))check =false;
                }
            }
        }
        if(check){
            fout<<"Case #"<<t<<": YES"<<endl;
        }else {
            fout<<"Case #"<<t<<": NO"<<endl;
        }

    }



}
