#include <iostream>
#include <string>
#include <cctype>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
    int T;
    ifstream fin("magictrick.in");
    ofstream fout("outtrick.out");
    fin >> T;
    for(int tt = 1; tt <= T; tt++) {
        int a, b, count = 0, ans;
        fin >> a;
        int cards[17];
        memset(cards, 0, sizeof cards);
        for(int i = 1; i <= 4; i++) {
            for(int j = 0; j < 4; j++) {
                int temp;
                fin >> temp;
                if(a == i){
                  cards[temp] = 1;
                }
            }
        }
        fin >> b;
        for(int i = 1; i <= 4; i++) {
            for(int j = 0; j < 4; j++) {
                int temp;
                fin >> temp;
                if(b == i && cards[temp]) {
                    ans = temp;
                    count++;
                }
            }
        }
        fout << "Case #" << tt << ": ";
        if(count == 1) {
            fout << ans << endl;
        }
        else if(count > 1) {
            fout << "Bad magician!" << endl;
        }
        else if(count == 0) {
            fout << "Volunteer cheated!" << endl;
        }
    }
    return 0;
}
