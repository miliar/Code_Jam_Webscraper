#include <istream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

void calculate(int t){
    int K, C, S;
    cin >> K >> C >> S;
    cout << "Case #" << t+1 << ":";
    for(int i = 0; i < K; i++){
        cout << " " << i+1;
    }
    cout << endl;
}

int main(){
    int T;
    cin>>T;
    for(int t = 0; t < T; t++){
        calculate(t);
    }
}
