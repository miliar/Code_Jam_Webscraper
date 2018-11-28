#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <unordered_map>
#include <algorithm>
using namespace std;
#define MP(x,y) make_pair(x,y)

bool static comparedesc(const long &stud1, const long &stud2){
    return stud1 > stud2;
}
int finalr[51][51], finalc[51][51];
bool triedr[51][51], triedc[51][51];
int N;
int maxInd;
int finalR, finalC;
bool copyR(vector<vector<int> > &inp, int ri, int ind){
    
    for(int j=0; j<N; j++){
        if((ri>0 && finalr[ri-1][j] >= inp[ind][j]) )
            return false;
        finalr[ri][j] = inp[ind][j];
    }
    return true;
}

bool copyC(vector<vector<int> > &inp, int ci, int ind){
    
    for(int j=0; j<N; j++){
        if( (ci>0 && finalc[j][ci-1] >= inp[ind][j])  )
            return false;
        finalc[j][ci] = inp[ind][j];
    }
    return true;
}

bool tryRow(vector<vector<int> > &inp, int r,  int ind, vector<bool> &done){
    //cout << "tryRow " << ind << "," << r << endl;
    if(r==N){
        finalC = N-1;
        int c = 0;
        int missed = 0;
        for(int i=0; i<2*N-1; i++){
            if(done[i]) continue;
            for(int j=0; j<N; j++){
                if(inp[i][j] != finalr[j][c]){
                    finalC = c;
                    missed++;
                    i--;
                    break;
                }
            }
            if(missed>1) return false;
            c++;
        }
        return true;
    }
    if(ind==maxInd) return false;
    if (maxInd - ind < N-r)
        return false;
    if(copyR(inp, r, ind)){
        done[ind] = true;
        if(tryRow(inp, r+1, ind+1, done))
            return true;
        done[ind] = false;
    }
    return (tryRow(inp, r, ind+1, done));
}

bool tryCol(vector<vector<int> > &inp, int c,  int ind, vector<bool> &done){
    //cout << "tryCol " << ind << "," << c << endl;
    
    if(c==N){
        finalR = N-1;
        int r = 0;
        int missed = 0;
        for(int i=0; i<2*N-1; i++){
            if(done[i]) continue;
            for(int j=0; j<N; j++){
                if(inp[i][j] != finalc[r][j]){
                    finalR = r;
                    missed++;
                    i--;
                    break;
                }
            }
            r++;
            if(missed>1) return false;
        }
        return true;
    }
    
    if(ind==maxInd) return false;
    if (maxInd-ind < N-c)
        return false;
    if(copyC(inp, c, ind)){
        done[ind] = true;
        if(tryCol(inp, c+1, ind+1, done))
            return true;
        done[ind] = false;
    }
    return (tryCol(inp, c, ind+1, done));
}


int main(){
    int t ;
    cin >> t;
    for(int _t=1; _t<=t; _t++){
        printf("Case #%d: ", _t);
        cin >> N;
        maxInd = 2*N-1;
        vector<vector<int> > inp(2*N-1, vector<int>(N,0));
        for(int i=0; i<2*N-1; i++){
            for(int j=0; j<N; j++){
                cin >> inp[i][j];
                //triedr[i][j] = triedc[i][j] = 0;
            }
        }
        sort(inp.begin(), inp.end());
        vector<bool> done(2*N+1, 0);
        if(tryRow(inp, 0, 0, done))
             for(int j=0; j<N; j++)
                cout << finalr[j][finalC] << " ";
        else if(tryCol(inp, 0, 0, done))
            for(int j=0; j<N; j++)
                cout << finalc[finalR][j] << " ";
        cout << endl;
    }
    return 0;
}