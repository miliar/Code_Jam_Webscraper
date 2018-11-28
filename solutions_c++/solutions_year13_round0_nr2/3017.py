#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
//#include <vector>
//#include <algorithm>
//#include <cassert>
using namespace std;
long N;
        long A,B;
int main() {
    std::ifstream fin ("B-large.in");
    std::ofstream fout("lawn.out");
    int grid[100][100];
    int aMax[100],bMax[100];
    fin>>N;
    for(long i=0;i<N;i++)
    {
        bool can=false;
        fout<<"Case #"<<(i+1)<<": ";
        fin>>A>>B;
        for(int i=0;i<A;i++)
        {
            for(int j=0;j<B;j++)
            {
                fin>>grid[i][j];
                if(grid[i][j]>aMax[i]) aMax[i]=grid[i][j];
                if(grid[i][j]>bMax[j]) bMax[j]=grid[i][j];
            }
        }
        for(int i=0;i<A;i++)
            for(int j=0;j<B;j++)
                if(grid[i][j]<aMax[i] && grid[i][j]<bMax[j])
                    goto here;  
        can=true;
        here:
        fout<<(can?"YES":"NO")<<"\n";
        for(int i=0;i<100;i++) {aMax[i]=0;bMax[i]=0;}
    }
    
    return 0;
}
