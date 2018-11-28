#include <bits/stdc++.h>

using namespace std;

unsigned long long answer(unsigned long long N) {
    unsigned long long ans, no;
    set<int> dig;
    for(unsigned long long i = 0; i < 100; i ++){
        ans = N * i;
        no = ans;
        while(no){
            dig.insert(no % 10);
            no /= 10;
        }
        if(dig.size() == 10)
            return ans;
    }
}

int main() {
    ifstream fileIn;
    ofstream fileOut;
    fileIn.open("A-large.in");
    fileOut.open("out.txt");
    int T;
    fileIn >> T;
    for(int i = 1; i <= T; i ++) {
        unsigned long long N;
        fileIn >> N;
        if(N == 0){
            fileOut << "Case #" << i << ": INSOMNIA\n";
        }
        else {
            fileOut << "Case #" << i << ": " << answer(N) << "\n";
        }
    }
    return 0;
}
