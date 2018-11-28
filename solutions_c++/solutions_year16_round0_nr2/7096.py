#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main() {
    ifstream cin("/Users/mayurpawar/Desktop/cpp/codejam/B-large.in");
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        int ans=0;
        cout << "Case #" << i+1 << ": ";
        string input;
        cin >> input;
        int len=(int)input.length();
        if (len==1 && input=="+") ans = 0;
        if (len==1 && input=="-") ans = 1;
        
        for (int i=1; i<len; i++) {
            if (input[i-1]!=input[i] && input[i]== '+') ans=ans+1;
            if (input[i-1]!=input[i] && input[i]== '-') {
                ans=ans+2;
                for (int j=i; j<len; j++) {
                    if (input[j]== '-') {
                        input[j]='+';
                        i++;
                    }
                    else break;
                }
            }
        }
    
        if (input[len-1]=='-' && ans==0) ans=1;
        cout << ans << endl;
    }
}