#include<bits/stdc++.h>
using namespace std;

int main(){
    freopen("inp.txt","r",stdin);

    freopen("out.txt","w",stdout);
    int T;
    string s;
    cin >> T;


    for(int k =0; k < T; k++){
        cin >> s;

        string a = "";

        a+=s[0];

        for(int l = 1; l < s.size();l++){
            if(s[l] < a[0]){
                a+=s[l];
            }
            else{
                string nn = "";
                nn+=s[l];
                nn+=a;
                //cout << "dbg: " << nn << endl;
                a = nn;
            }

        }

        cout << "Case #" << k+1 << ": " << a << endl;

    }
}
