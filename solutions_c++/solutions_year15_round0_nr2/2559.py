#include <stdio.h>
#include <iostream>
#include <fstream>
#include <set>
#include <map>

using namespace std;

int t, l;
set<int> numS;
map<int, int> numM;

int main(){
    ifstream in;
    in.open("in.txt");
    ofstream out;
    out.open("out.txt");
    in >> t;
    for (int i = 0 ; i < t ; ++i) {
        in >> l;
        int a;
        numS.clear();
        numM.clear();
        for (int j = 0 ; j < l ; ++j) {
            in >> a;
            numM[a] += 1;
            numS.insert(a);
        }
        bool justOK = true;
        int step = 0;
        int maxNum = 0;
        int curDepCount = 0;
        int curDep = 0;
        while (true) {
            if (justOK) {
                maxNum = *numS.rbegin();
                numS.erase(maxNum);
                if (maxNum < 2) {
                    step += maxNum;
                    break;
                }
                curDepCount = numM[maxNum];
                if (curDepCount != 1) {
                    numS.insert(maxNum / 2);
                    numS.insert(maxNum - maxNum/2);
                    numM[maxNum / 2] += curDepCount;
                    numM[maxNum - maxNum/2] += curDepCount;
                    justOK = false;
                } else {
                    if (maxNum == 9 && (numS.rbegin() == numS.rend() || *numS.rbegin() < 4
                                        || (*numS.rbegin() == 6 && numM[6] == 1 && numM[5] == 0 && numM[4] == 0))) {
                        numS.insert(3);
                        numS.insert(6);
                        numM[3] += curDepCount;
                        numM[6] += curDepCount;
                    } else {
                        numS.insert(maxNum / 2);
                        numS.insert(maxNum - maxNum/2);
                        numM[maxNum / 2] += curDepCount;
                        numM[maxNum - maxNum/2] += curDepCount;
                    }
                    step += 1;
                }
                continue;
            }
            curDep = *numS.rbegin();
            if (curDep < maxNum - curDepCount + 1) {
                justOK = true;
                step += curDepCount;
            } else {
                curDepCount += numM[curDep];
                if (curDepCount > maxNum) {
                    step += maxNum;
                    break;
                }
                numS.insert(curDep / 2);
                numS.insert(curDep - curDep/2);
                numM[curDep / 2] += numM[curDep];
                numM[curDep - curDep/2] += numM[curDep];
                numS.erase(curDep);
            }
        }
        out << "Case #" << i + 1 << ": " << step << endl;
    }
    in.close();
    out.close();
}