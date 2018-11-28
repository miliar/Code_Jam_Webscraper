#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


bool isValid(vector<vector<int> > &area, int R, int C, int r, int c)
{
    
    int up=1, lw=1, lf=1, rt=1;
    int i=0;
    
    for( i=0; i<R; i++) {
        if(i<r){
        	 if( area[i][c] > up) {
        	 	up = area[i][c];
        	}
        }
        if(i>r){
        	 if( area[i][c] > lw) {
        	 	lw = area[i][c];
        	}
        }
    }
    
    for( i=0; i<C; i++) {
        if(i<c){
        	 if( area[r][i] > lf) {
        	 	lf = area[r][i];
        	}
        }
        if(i>c){
        	 if( area[r][i] > rt) {
        	 	rt = area[r][i];
        	}
        }
    }

 		if(( area[r][c]>=lf && area[r][c] >= rt) || ( area[r][c]>=up &&  area[r][c]>= lw))
        return true;
    else return false;

}

int main(int argc, char* argv[])
{
    int N, M, T=0;
    
    vector<vector<int> > area;
    ifstream fin;
    ofstream fout;
    bool possible;


    fin.open(argv[1], ifstream::in);
    fout.open("output.txt", ofstream::out);

    fin >> T;

    for(int t=0; t < T; t++) {
        possible = true;

        fin >> N;
        area.resize(N);

        fin >> M;
        
        for(int n=0; n<N; n++) {
            area[n].resize(M);
            for(int m=0; m<M; m++) {
                fin >> area[n][m];
            }
        }
        
        for(int n=0; n<N; n++) {
            for(int m=0; m<M; m++) {
               if(!isValid(area, N, M, n, m))
                   possible = false;
            }
        }
        if(possible)
            fout << "Case #" << t+1 << ": " << "YES" << endl;
        else
            fout << "Case #" << t+1 << ": " << "NO" << endl;
    }

    fin.close();
    fout.close();

    return 0;
}
