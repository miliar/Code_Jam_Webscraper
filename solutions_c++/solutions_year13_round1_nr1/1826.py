#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;
typedef unsigned long long ULL;

int main(){
    ofstream fout ("bullseye.out");
    ifstream fin ("bullseye.in");
    ULL T;
    fin >> T;
    
    for(int i = 0; i < T; i++){
        ULL r, t;
        ULL n = 0;
        ULL area;
        fin >> r >> t;
        while(true){
            area = 2 * n * n + n * (2 * r - 1);
            if(area > t){
                break;
            }
            n++;
        }
        fout << "Case #" << (i + 1) << ": " << (n-1) << endl;
    }
}
    
        
