#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
#include <iomanip>
using namespace std;

bool isValid(string s){
    for(auto & c : s){
        if (c != '+'){
            return false;
        }
    }
    return true;
}
int main(){
    int n;
    string w;
    cin >> n;
    for(int i = 1; i <= n; i++){
        cin >> w;
        int flipTimes = 0;
        int j = 0;
        while(!isValid(w)){
            if(w.size() == 0){
                flipTimes = 1;
                break;
            }
            for(;j < w.size(); j++){
                    if(j > 0 and w[j] == '-' and w[j - 1] == '+'){
                        flipTimes++;
                        for(int k = 0; k < j; k ++){
                            w[k] = '-';
                        }
                        break;
                    }else if(j > 0 and w[j - 1] == '-' and w[j] == '+'){
                        flipTimes ++;
                        for(int k = 0; k < j; k ++){
                            w[k] = '+';
                        }
                        break;
                    }
            }
            if(j == w.size()){
                if(w[w.size()-1] == '-'){
                    flipTimes ++ ;
                    break;
                }
            }
        }
        cout << "Case #" << i << ": " << flipTimes << endl;
    }
    return 0;
}
