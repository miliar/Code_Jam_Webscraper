#include <iostream>
#include <fstream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
ifstream fin("war.in"); ofstream fout("war.out");
const int MAXN = 1000;
double n[MAXN], k[MAXN];
bool nu[MAXN], ku[MAXN];

int main(){
    int T;
    fin >> T;
    for(int cases = 1; cases <= T; cases++){
        int N;
        fin >> N;
        for(int i = 0; i < N; i++) fin >> n[i];
        sort(n, n + N);
        memset(nu, 0, sizeof(nu));
        for(int i = 0; i < N; i++) fin >> k[i];
        sort(k, k + N);
        memset(ku, 0, sizeof(ku));
        int warPts = 0;
        for(int i = 0; i < N; i++){ //Normal war
            int use = -1;
            for(int j = 0; j < N; j++){
                if(ku[j]) continue;
                if(k[j] > n[i]){
                    use = j;
                    ku[j] = true;
                    break;
                }
            }
            if(use == -1) warPts++;
        }

        //Deceitful war
        int dWarPts = N;
        for(int i = 0; i < N; i++){
            int use = -1;
            for(int j = 0; j < N; j++){
                if(nu[j]) continue;
                if(n[j] > k[i]){
                    use = j;
                    nu[j] = true;
                    break;
                }
            }
            if(use == -1) dWarPts--;
        }
        fout << "Case #" << cases << ": " << dWarPts << " " << warPts << endl;
    }
}
