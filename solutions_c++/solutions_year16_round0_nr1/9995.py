#include <cstdio>
#include <set>
#include <iostream>
using namespace std;

int main(){
    int noOfTestCases = 0, curStartNum = 0, curNum = 0, curCntr = 10, curDigit = 0;
    set<int> curDoneDigits;
    cin >> noOfTestCases;
    
    for(int cntr = 1; cntr <= noOfTestCases; cntr++){
        curStartNum = 0, curNum = 10, curCntr = 0;
        curDoneDigits.clear();
        cin >> curNum;

        if(curNum > 0) {
            while(curDoneDigits.size() < 10) {
                curStartNum = ++curCntr * curNum;
                
                while(curStartNum >= 10) {
                    curDigit = curStartNum % 10;
                    curDoneDigits.insert(curDigit);
                    curStartNum /= 10;
                }
                curDoneDigits.insert(curStartNum);
            }
            cout << "Case #" << cntr << ": " << curCntr-- * curNum << endl;
        } else {
            cout << "Case #" << cntr << ": INSOMNIA" << endl;
        }

    }
    return 0;
}