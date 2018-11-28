#include <iostream>
#include <string>
#include <queue>
using namespace std;

void printResult(int caseNum, string result){
    cout<<"Case #"<<caseNum<<": "<<result<<endl;
}

int matrix(int x, int y){
    int factor = 1;
    if (x < 0) {
        x = 0 - x;
        factor *= -1;
    }
    if (y < 0) {
        y = 0 - y;
        factor *= -1;
    }
    
    int result = 1;
    if (x == '1') {
        result = y;
    }
    else if (y == '1') {
        result = x;
    }
    else if (x == y) {
        result = 0 - '1';
    }
    else if (x == 'i' && y == 'j') {
        result = 'k';
    }
    else if (x == 'j' && y == 'i') {
        result = 0 - 'k';
    }
    else if (x == 'j' && y == 'k') {
        result = 'i';
    }
    else if (x == 'k' && y == 'j') {
        result = 0 - 'i';
    }
    else if (x == 'i' && y == 'k') {
        result = 0 - 'j';
    }
    else if (x == 'k' && y == 'i') {
        result = 'j';
    }
    return factor * result;
}

int main(int argc, const char * argv[])
{
    int T;cin>>T;
    for (int kk = 1; kk <= T; ++ kk) {
        int L,X;
        string s;
        cin>>L>>X>>s;
        
        string t = "";
        for (int i = 0; i < X; ++ i) {
            t = t + s;
        }
        int index1 = t.size() + 10;
        int index2 = -1;
        int product = '1';
        for (int i = 0; i < t.size(); ++ i) {
            product = matrix(product, t[i]);
            if (product == 'i') {
                index1 = index1 > i ? i : index1;
            } else if(product == 'k'){
                index2 = index2 < i ? i : index2;
            }
        }
        if (index1 < index2 && product == 0 - '1') {
            printResult(kk, "YES");
        } else{
            printResult(kk, "NO");
        }
    }
}

