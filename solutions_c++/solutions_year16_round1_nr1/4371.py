// Author:   Charles AUGUSTE

#include <iostream>
#include <fstream>
#include <math.h>
#include <sstream>
#include <stdlib.h>

using namespace std;

int main(){
    int T;
    cin >> T;
    for (int i=0; i<T; ++i){
        string S;
        string res;
        cin >> S;
        cout << "Case #" << i+1 << ": ";
        if (S!=""){
            res=S[0];
            for (int i=1; i<S.size(); ++i){
                if (S[i]>=res[0]){
                    res=S[i]+res;
                }
                else
                    res=res+S[i];
            }

        }
        cout << res << endl;
    }
    return 0;
}
