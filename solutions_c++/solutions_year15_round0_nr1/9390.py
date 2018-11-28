#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ofstream out;
    ifstream in;
    in.open("A-large.in");
    out.open("output.out");
    int t;
    in>>t;
    for (int testNum = 0; testNum < t; testNum++){
        int mostShy; in>>mostShy;
        string lst; in>>lst;
        int standing[10001] = {0};
        int st = 0;
        for (int i = 0; i < mostShy+1; i++){
            int a = (int)(lst[i] - '0');
            for (int j = 0; j < a; j++){
                standing[st] = i;
                st++;
            }
        }

        int addNum = 0;
        for (int i = 0; i < st; i++){
            addNum = addNum < (standing[i] - i)?(standing[i] - i):addNum;
        }

        out<<"Case #"<<(testNum + 1)<<": "<<addNum<<endl;
    }
    in.close();
    out.close();
    return 0;
}
