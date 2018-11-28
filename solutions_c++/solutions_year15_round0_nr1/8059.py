#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

int run() {
    int caseNum = 0;
    cin >> caseNum;
    for(int i = 1; i <= caseNum; i ++) {
        int shyLevel = 0;
        string shyStr;
        cin >> shyLevel >> shyStr;
        if(shyLevel <= 0) {
            printf("Case #%d: %d\n", i, 0);
        }
        else {
            int inviteNum = 0;
            int curNum = (shyStr[0] - '0');
            for(int j = 1; j < shyStr.size(); j ++) {
                if(j > curNum) {
                    inviteNum += (j - curNum);
                    curNum = j;
                }
                curNum += (shyStr[j] - '0');
            }
            printf("Case #%d: %d\n", i, inviteNum);
        }
    }
    return 0;
}

int main(int argc, char * argv[]) {
    run();
    return 0;
}


