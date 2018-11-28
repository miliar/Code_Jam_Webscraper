#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <math.h>
#include <stdlib.h>

using namespace std;

long long power(int a, int n) {
    long long result = 1;
    for (int i=0;i<n;i++) {
        result *= a;
    }
    return result;
}

int main() {
    ifstream fin ("/Users/LeonardNguyen/Documents/projects/ios/usaco/D-small-attempt2.in");
    
    int T;
    fin>>T;
    
    for (int i=0;i<T;i++) {
        int K, C, S;
        fin >> K >> C >> S;
        cout<<"Case #"<<(i+1)<<":";
        for (int j=0;j<S;j++) {
            //cout<<" "<<j*power(K,C-1)+1;
            cout<<" "<<j+1;
        }
        cout<<endl;
    }
    
    fin.close();
    return 0;
}

