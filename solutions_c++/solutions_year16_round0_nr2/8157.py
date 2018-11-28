#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("/home/aman/Downloads/input.in","r",stdin);
    freopen("/home/aman/Downloads/output.txt","w",stdout);
    int t;
    cin >> t;
    for(int test=1;test<=t;test++){
        string S;
        cin >> S;
        int i=1,l = S.length();
        int cnt=0;
        while(i<l){
            if(S[i]==S[i-1]){
                i++;
            }
            else {
                cnt++;
                reverse(S.begin(),S.begin()+i-1);
                for(int j=0;j<i;j++){
                    if(S[j]=='+'){
                        S[j]='-';
                    }
                    else {
                        S[j]='+';
                    }
                }
                i=1;
            }
        }
        if(S[0]=='-'){
            cnt++;
        }

        cout << "Case #" << test << ": " << cnt << endl;
    }
    return 0;
}