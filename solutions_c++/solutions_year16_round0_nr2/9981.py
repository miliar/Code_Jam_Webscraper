#include<bits/stdc++.h>

using namespace std;

int main(){
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin >> t;
    for(int p=1;p<=t;p++){
        string s;
        cin >> s;
        int l = s.length();
        int flag = 0;
        if(s[0]=='-'){
            flag = 0;
        }
        else{
            flag = 1;
        }
        string aux = "";
        aux = aux + s[0];
        int flips = 0;
        for(int i=1;i<l;i++){
            if(s[i-1]!=s[i]){
                flag = 1-flag;
                flips++;
            }
        }
        if(flag==0){
            flips++;
            flag = 1;
        }
        cout << "Case #" << p << ": " << flips << endl;
    }

return 0;
}
