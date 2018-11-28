#include<fstream>
using namespace std;

ifstream fin("lawnmower.in");
ofstream fout("lawnmower.out");

int T, N, M;
int m1[105], m2[105];
int g[105][105];

int main(){
    fin >> T;
    for(int t=0; t<T; t++){
        for(int q=0; q<100; q++)
            m1[q] = m2[q] = 0;
        fin >> N >> M;
        for(int n=0; n<N; n++)
            for(int m=0; m<M; m++){
                fin >> g[n][m];
                if(g[n][m] > m1[n]) m1[n] = g[n][m];
                if(g[n][m] > m2[m]) m2[m] = g[n][m];
            }
        bool works = true;
        for(int n=0; n<N; n++)
            for(int m=0; m<M; m++)
                if(g[n][m] < m1[n] && g[n][m] < m2[m])
                    works = false;
        fout << "Case #" << t+1 << ": ";
        if(works) fout << "YES" << endl;
        else fout << "NO" << endl;
    }
}
