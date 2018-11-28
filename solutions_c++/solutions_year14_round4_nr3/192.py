#include<fstream>
#include<map>
using namespace std;

ifstream fin("nile.in");
ofstream fout("nile.out");

int T, W, H, B;
int build[1005][4];
int dist[1005][1005];
int done[1005];
int shrt[1005];

int ans(){
    shrt[0] = 0;
    for(int i=1; i<B; i++)
        shrt[i] = 1000000007;
    memset(done, 0, sizeof(done));
        
    int D = B;
    while(D){
        int cand = 0;
        while(done[cand]) cand++;
        for(int j = cand+1; j<B; j++)
            if(!done[j] && (shrt[j] < shrt[cand]))
                cand = j;
        
        done[cand] = true;
        D--;
        
        for(int i=0; i<B; i++)
            shrt[i] = min(shrt[i], shrt[cand] + dist[cand][i]);
    }
    
    return shrt[B-1];
}

int main(){
    int T;
    fin >> T;
    for(int t=0; t<T; t++){
        
        fin >> W >> H >> B;
        
        build[0][0] = -1;
        build[0][1] = 0;
        build[0][2] = -1;
        build[0][3] = H-1;
        
        for(int i=1; i<=B; i++)
            for(int j=0; j<4; j++)
                fin >> build[i][j];
                
        build[B+1][0] = W;
        build[B+1][1] = 0;
        build[B+1][2] = W;
        build[B+1][3] = H-1;
        
        B += 2;
        
        for(int i=0; i<B; i++)
            for(int j=0; j<B; j++){
                if(i == j) dist[i][j] = 1;
                else{
                    dist[i][j] = 1000000007;
                    
                    //can go same row
                    if(max(build[i][1], build[j][1]) <= min(build[i][3], build[j][3])){
                        dist[i][j] = min(dist[i][j], min(abs(build[i][2] - build[j][0]), abs(build[j][2] - build[i][0]))); }
                        
                    //can go same col
                    if(max(build[i][0], build[j][0]) <= min(build[i][2], build[j][2])){
                        dist[i][j] = min(dist[i][j], min(abs(build[i][1] - build[j][3]), abs(build[j][1] - build[i][3]))); }
                        
                    //cannot do either
                    int lef = (build[i][2] < build[j][0])? i : j;
                    int rig = i + j - lef;
                    
                    //top right of left to bottom left of right
                    {
                        int dx = abs(build[lef][2] - build[rig][0]);
                        int dy = abs(build[lef][3] - build[rig][1]);
                        int diag = min(dx, dy);
                        dist[i][j] = min(dist[i][j], dx + dy - diag);
                    }
                    
                    //bottom right of left to top left of right
                    {
                        int dx = abs(build[lef][2] - build[rig][0]);
                        int dy = abs(build[lef][1] - build[rig][3]);
                        int diag = min(dx, dy);
                        dist[i][j] = min(dist[i][j], dx + dy - diag);
                    }
                }
                
                dist[i][j]--;
                
            }
                
        fout << "Case #" << t+1 << ": ";
        fout << ans() << endl;
    }
}
