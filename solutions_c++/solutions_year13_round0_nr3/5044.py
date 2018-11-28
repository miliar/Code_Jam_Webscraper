#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

bool isFair(int n){
    if(n < 10){
        return true;
    }
    ostringstream n_ss;
    n_ss << n;
    string s = n_ss.str();
    int N = s.size() - 1; // Last element index
    for(int i = 0; i < int(N/2) + 1; i++){
        if(s[i] != s[N-i]){
            return false;
        }
    }
    return true;
}

int main(int argc, char** argv){
    ifstream in;
    in.open(argv[1]);

    int cases;
    in >> cases;
    
    int a, b, count, caseN;
    caseN = 1;
    while(in >> a >> b){
        count = 0;
        //cout << "a: " << a << " b: " << b << "\n";
        for(int i = ceil(sqrt(a)); i <= sqrt(b); i++){
            bool cand = isFair(i);
            //cout << i << " is " << cand << "\n";
            if(cand && isFair(i * i)){
                    count++;
                    //cout << "Found: " << i * i << "\n";
            }
        }
        cout << "Case #" << caseN << ": " << count << "\n";
        caseN++;
    }
}
