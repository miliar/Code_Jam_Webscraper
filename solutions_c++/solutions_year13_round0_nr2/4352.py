#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("b.out");

int main() {
    int T , map[110][110], kase = 1;
    fin >> T;
    while(T--) {
        bool flag = true;
        int n , m , maxValue = 0 , max2Value = 0, cnt = 0;
        fin >> n >> m;
        for(int i = 1 ; i <= n ; i++)
            for(int j = 1 ; j <= m ; j++) {fin >> map[i][j]; maxValue = map[i][j] > maxValue ? map[i][j] : maxValue;}
        while(cnt < n*m) {
            for(int i = 1 ; i <= n ; i++)
                for(int j = 1 ; j <= m ; j++) {
                    if(map[i][j] == maxValue) { map[i][j] = -1; cnt++;}
                    max2Value = (map[i][j] > max2Value && map[i][j] < maxValue)?map[i][j] : max2Value;
                }
            for(int i = 1 ; i <= n ; i++) {
                for(int j = 1 ; j <= m ; j++) {
                    int kkk = 0;
                    if(map[i][j] == max2Value) {
                        for(int k = 1 ; k <= n ; k++) {
                            if(k == i) continue;
                            if(map[k][j] == -1) { kkk++; break;}
                        }
                        for(int k = 1 ; k <= m ; k++) {
                            if(k == j) continue;
                            if(map[i][k] == -1) { kkk++; break;}
                        }
                        //fout << i << ' ' << j << ' ' << kkk <<endl;
                        if(kkk == 2) {flag = false; break;}
                    }
                }
                if(flag == false) break;
            }

            maxValue = max2Value;
            max2Value = 0;
            if(flag == false) break;
        }
        if(flag == false) fout << "Case #" << kase++ <<": NO" << endl;
        else fout << "Case #" << kase++ << ": YES" << endl;
    }
    return 0;
}
