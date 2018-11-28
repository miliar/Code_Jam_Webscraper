#include <iostream>
using namespace std;



int main(){
    int tests;
    cin >> tests;
    for (int test =1; test <= tests; test++){
        int ans = 0;
        int standing = 0;
        int ms;
        cin >> ms;
        for (int shy=0;shy<=ms;shy++){
            int num;
            char c;
            cin >> c;
            num = c - '0';
            for (int j=0;j<num;j++){
                if (standing < shy){
                    ans += (shy - standing);
                    standing = shy;
                }
                standing += 1;
            }
        }
        cout << "Case #" << test << ": " << ans << endl;

    }
    
    
}