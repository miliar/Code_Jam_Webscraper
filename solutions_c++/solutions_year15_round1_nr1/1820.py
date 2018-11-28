#include<fstream>
#include<iostream>
#include<cstdlib>
#include<cmath> 
#include<algorithm>
#include<vector>
#include<list>
#include<cstring>
#include<stack>
#include<map>
#include<set>
#include<utility>
#include<queue>
#include<deque>
#include<ctime>
#include<complex>
#include<bitset>

using namespace std;
#define PB push_back
#define LL long long
#define MP make_pair

ifstream fin("A-large.in");
ofstream fout("A-large.out");
int T,N;
int y,z,imax;
int mush[10000];//<=1000
int main(void){
    fin >> T;
    for(int i=1;i<=T;i++){
        fin >> N;
        for(int j=0;j<N;j++){
            fin >> mush[j];
        }
        int l = N;
        y=0;
        imax=0;
        int a;
        for(int j=0;j<l-1;j++){
            if(mush[j]>mush[j+1]){
                a=mush[j]-mush[j+1];
                y+=a;
                if(a>imax){
                    imax=a;
                }
            }
        }
        z=0;
        for(int j=0;j<l-1;j++){
            if (mush[j]>=imax){
                z+=imax;
            }
            else{
                z+=mush[j];
            }
        }
        fout << "Case #" << i << ": " << y << ' ' << z << endl;
    }
    return 0;
}

