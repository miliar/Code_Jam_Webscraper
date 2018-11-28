#include <cstdio>
#include <fstream>
#include <stdint.h>
#include <algorithm>
#define for0(i, n) for(int i = 0; i < n; i++)
using namespace std;

struct Triple{
    int v, i, j;
    Triple(int v = 0, int i = 0, int j = 0):v(v), i(i), j(j){}
};
bool moreThan(const Triple &a, const Triple &b){
    return a.v > b.v;
}
int a[100][100];
int cur[100][100];
Triple array[10000];
int main() {
    ifstream in("common.in");
    ofstream out("common.out");
    int testCount, n, m;
    in>>testCount;

    for0(k, testCount){
        out<<"Case #"<<(k + 1)<<": ";
        in>>n>>m;
        int c = 0;
        for0(i, n){
            for0(j, m){
                in>>a[i][j];
                cur[i][j] = 100;
                array[c++] = Triple(a[i][j], i, j);
            }
        }
        sort(array, array + c, moreThan);
        bool flag = true;
        for(int i = 0; i < c && flag; i++){
            int I = array[i].i, J = array[i].j, V = array[i].v;
            if(V == cur[I][J]){
                continue;
            }
            bool can = true;
            for0(j, m){
                if(a[I][j] > V){
                    can = false;
                    break;
                }
            }
            if(can){
                for0(j, m){
                    cur[I][j] = V;
                }
            } else {
                bool can1 = true;
                for0(j, n){
                    if(a[j][J] > V){
                        can1 = false;
                        break;
                    }
                }
                if(can1){
                    for0(j, n){
                        cur[j][J] = V;
                    }
                } else {
                    flag = false;
                }
            }
        }

        out<<(flag ? "YES" : "NO")<<"\n";
    }
    return 0;
}
