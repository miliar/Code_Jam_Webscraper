#include <iostream>
#include <cstring>

using namespace std;

char stri[101];

int calculate(int length){
    int i = length - 1;
    int count = 0;
    while (i >= 0){
        if (stri[i] == '-'){
            count++;
            break;
        }
        i--;
    }
    while (i > 0){
        if (stri[i] == stri[i-1])
            i--;
        else{
            count++;
            i--;
        }
    }
    return count;
}

int main(){
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++){
        cin >> stri;
        int res = calculate(strlen(stri));
        cout << "Case #" << i << ": " << res << "\n";
    }
    return 0;
}
