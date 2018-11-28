#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

bool end(char* c, int size){
    bool end = false;
    for(int i=0; i<size; i++){
        if(c[i]!='+'){
            break;
        }
        else if(i==size-1){
            end = true;
        }
    }
    return end;
}

char inverse(char c){
    if(c=='+') return '-';
    if(c=='-') return '+';
}

void change(char* c, int i){
    string copy(c);
    char* b = const_cast<char*>(copy.c_str());
    for(int k=i, j=0; k>=0; k--, j++){
        c[k] = inverse(b[j]);
    }
}

int getResult(string pancakes){
    int result = 0;
    int size = pancakes.size();
    char* c = const_cast<char*>(pancakes.c_str());
    while(!end(c, size)){    
        if(c[0]=='+'){
            for(int r=0; r<size; r++){
                if(c[r]=='+'){
                    c[r]='-';
                }
                else break;
            }
            result++;
        }
        for(int i=size-1; i>=0; i--){
            if(c[i]=='-'){
                change(c, i);
                result++;
                break;
            }
        }
    }
    return result;
}

int main() {
    int t, result;
    cin >> t;
    for (int i = 1; i <= t; ++i){
        string pancakes = "";
        cin >> pancakes;
        result = getResult(pancakes);
        cout << "Case #" << i << ": " << result << endl;
    }
}
