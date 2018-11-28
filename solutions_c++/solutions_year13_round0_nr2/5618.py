#include <iostream>
#include <fstream>

#define cin fin
#define cout fout

using namespace std;

ifstream fin("input2.in");
ofstream fout("output");

bool check(int **grid,int *maxr,int *maxc,int M,int N){

        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(maxr[i]>grid[i][j] && maxc[j]>grid[i][j]){
                    return false;
                }
            }
        }
    return true;
}

int main()
{
    int T,M,N,**grid=new int*[100],*maxr,*maxc;
    for(int i=0;i<100;i++)
        grid[i]=new int[100];
    cin >> T;
    for(int c=1;c<=T;c++){
        maxr=new int[100]();
        maxc=new int[100]();
        cin >> N >> M;
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                cin >> grid[i][j];
                if(maxr[i]<grid[i][j])
                    maxr[i]=grid[i][j];
                if(maxc[j]<grid[i][j])
                    maxc[j]=grid[i][j];
            }
        }
        cout << "Case #"<< c << ": ";
        if(check(grid,maxr,maxc,M,N)){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }
    }
    return 0;
}
