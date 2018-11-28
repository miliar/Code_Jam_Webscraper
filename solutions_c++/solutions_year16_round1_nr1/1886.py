#include <iostream>
#include <cstring>
using namespace std;
void solveAndPrint(const string &str, int caseNum);
int main(int argc, char *argv[]) {
    int numOfCase;
    cin >> numOfCase;
    string str;
    for (int i = 0; i < numOfCase; i++) {
        cin >> str;
        solveAndPrint(str, i + 1);
    }
}

void solveAndPrint(const string &str, int caseNum) {
    char head;
    string result;
    auto iter = str.begin();
    auto endIter = str.end();
    head = *iter++;
    result.push_back(head);
    string tmpStr;
    while (iter != endIter) {
        if (*iter >= head) {
            tmpStr.push_back(*iter);
            result = tmpStr + result;
            head = *iter;
            tmpStr="";
        } else {
            result.push_back(*iter);
        }
        iter++;
    }
    cout<<"Case #"<<caseNum<<": "<<result<<endl;
}
