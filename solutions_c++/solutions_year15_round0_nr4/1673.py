#include <iostream>
#include <string>
#include <queue>
using namespace std;

void printResult(int caseNum, string result){
    cout<<"Case #"<<caseNum<<": "<<result<<endl;
}

int main(int argc, const char * argv[])
{
    int T;cin>>T;
    for (int kk = 1; kk <= T; ++ kk) {
        int x, r, c;cin>>x>>r>>c;
        if (x == 1) {
            printResult(kk, "GABRIEL");
        } else if(x == 2){
            if ((r * c) % 2 == 0) {
                printResult(kk, "GABRIEL");
            } else {
                printResult(kk, "RICHARD");
            }
        } else if(x == 3){
            if ((r * c) % 3 != 0) {
                printResult(kk, "RICHARD");
                continue;
            }
            int rest = (r * c) / 3;
            if (rest == 1) {
                printResult(kk, "RICHARD");
            } else {
                printResult(kk, "GABRIEL");
            }
        } else if(x == 4){
            if ((r * c) % 4 != 0 || (r == c && c == 2)) {
                printResult(kk, "RICHARD");
                continue;
            }
            int rest = (r * c) / 4;
            if (rest == 1) {
                printResult(kk, "RICHARD");
            } else if (rest == 2) {
                printResult(kk, "RICHARD");
            } else if (rest == 3) {
                printResult(kk, "GABRIEL");
            } else if (rest == 4) {
                printResult(kk, "GABRIEL");
            }
        }
    }
}

