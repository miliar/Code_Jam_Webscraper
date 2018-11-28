#include <iostream>
#include <vector>
//#include <algorithm>
#include <string>
//#include <stack>
#include <unordered_map>
//#include <limits.h>
#include <time.h>
//#include <queue>
#include <fstream>
using namespace std;


int main(){
    unsigned int t, k, c, s;
    cin >> t;
    for(int z = 0; z < t; ++z){
        cin >> k >> c >> s;
        unsigned long* pos = new unsigned long[k];
        for(int i = 0; i < k; ++i)  pos[i] = i + 1;
        for(int j = 1; j < c; ++j){
            for(int i = 0; i < k; ++i){
                pos[i] = (pos[i] - 1) * k + (i + 1);
            }
        }
        cout << "Case #" << z + 1 << ":";
        for(int i = 0; i < k; ++i) cout << ' ' << pos[i];
        cout << endl;
        delete [] pos;
    }
}