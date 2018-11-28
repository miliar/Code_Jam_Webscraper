#include<bits/stdc++.h>
using namespace std;
int main(){

    ofstream output;


    int t = 0,T;
    cin >> T;
    output.open ("output.txt",ios::app);
    while(T--){
        int S,cntF = 0,shyLess = 0;
        int str[10000];
        cin >> S;
        for(int i = 0; i <= S; i++){
            scanf("%1d",&str[i]);
        }
        shyLess = str[0];
        for(int i = 1; i <= S; i++){
            if(shyLess >= i){
                shyLess+=str[i];
            }
            else {
                cntF++;
                shyLess+=str[i]+1;
            }
        }
        output << "Case #" << ++t << ": " << cntF << endl;
    }
    output.close();
    return 0;
}
