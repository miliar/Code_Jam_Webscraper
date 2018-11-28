#include <iostream>
#include <fstream>

using namespace std;

int list[] = {1,4,9,121,484};
int T,A,B;

int main(int argc, char* argv[]) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    fin >> T;
    for(int tt = 1; tt <= T; tt++) {
        fin >> A >> B;
        int cnt = 0;
        for(int i = 0; i < 5; i++) {
            if(list[i] >= A && list[i] <= B) cnt++;
        }
        fout << "Case #" << tt << ": " << cnt << endl;
    }
    
    
    return 0;
}
