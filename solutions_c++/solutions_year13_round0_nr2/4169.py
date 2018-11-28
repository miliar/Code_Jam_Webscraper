#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool validField(vector<vector<int> > &lawn, int N, int M, int n, int m)
{
    int max_u = 1;
    int max_d = 1;
    int max_l = 1;
    int max_r = 1;
    int fld = lawn[n][m];

    //up/down
    for(int i=0; i<N; i++) {
        if(i<n && lawn[i][m] > max_u) max_u = lawn[i][m];
        if(i>n && lawn[i][m] > max_d) max_d = lawn[i][m];
    }

    //left/right
    for(int i=0; i<M; i++) {
        if(i<m && lawn[n][i] > max_l) max_l = lawn[n][i];
        if(i>m && lawn[n][i] > max_r) max_r = lawn[n][i];
    }
   
    if((max_l > fld || max_r > fld) && (max_u > fld || max_d > fld))
        return false;

    return true;
}

/* main program logic */
int main(int argc, char* argv[])
{
    if(argc < 2) {
        cout << "No input file provided" << endl;
        return 1;
    }

    /* open files */
    ifstream fin(argv[1], ifstream::in);
    ofstream fout("out.txt", ofstream::out);

    /* get testcase count */
    int T = 0;
    fin >> T;

    /* process testcases */
    for(int t=0; t < T; t++) {
        int N;
        int M;
        
        /* get lawn size */
        fin >> N >> M;
        
        vector<vector<int> > lawn;
        lawn.resize(N);
        
        /* read lawn pattern */
        for(int n=0; n<N; n++) {
            lawn[n].resize(M);
            for(int m=0; m<M; m++) {
                fin >> lawn[n][m];
            }
        }
       
        bool validLawn = true;

        /* check lawn patternt */
        for(int n=0; n<N; n++) {
            for(int m=0; m<M; m++) {
               if(!validField(lawn, N, M, n, m))
                   validLawn = false;
            }
        }

        fout << "Case #" << t+1 << ": " << (validLawn ? "YES" : "NO") << endl;

    }

    fin.close();
    fout.close();

    return 0;
}
