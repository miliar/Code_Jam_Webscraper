#include <iostream>
#include <string>

using namespace std;

#define N (100)
int sa[N];

int main(){
    int T,i,j,k,l,m,n;
    string S;
    cin >> T;
    for(i=0; i<T; i++){
        cin >> S;
        n = S.length();
        if(n==1){
            if(S[0]=='-'){
                cout << "Case #" << (i+1) << ": " << 1 << endl;
            }else{
                cout << "Case #" << (i+1) << ": " << 0 << endl;
            }
            continue;
        }
        int sum = 0;
        for(j=1; j<n; j++){
            if(S[j-1]==S[j]){
                continue;
            }else{
                sum++;
            }
        }
        if(S[n-1]=='-'){
            sum++;
        }
        cout << "Case #" << (i+1) << ": " << sum << endl;
    }
    return 0;
}
