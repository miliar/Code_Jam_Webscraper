#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
    int T, N,Loop1,Loop2;
    float G[1000], B[1000];
    ifstream fin("D-large (3).in");
	ofstream fout("namenum.out");
    fin>>T;
    for(int i=1; i<=T; i++){
        int War=0,DWar=0,success=0,factor=0;
        fin>>N;
        for (int j=0; j<N; j++)
            fin>>G[j];
        for (int j=0; j<N; j++)
            fin>>B[j];
        sort(G, G+N);
        sort(B, B+N);
        for(Loop1=0; Loop1<N-factor; Loop1++){
                 if(G[Loop1+factor]>B[Loop1])
                    DWar++;
                else {
                        Loop1--;
                        factor++;
                }
        }
        for(Loop1=N-1,Loop2=N-1; Loop1>=0; Loop1--){
            if(G[Loop1]>B[Loop2])
                War++;
            else Loop2--;
        }
        fout<<"Case #"<<i<<": "<<DWar<<" "<<War<<"\n";
    }
    return 0;
}
