#include <bits/stdc++.h>
#define FI freopen("test.in", "r", stdin); freopen("test.out", "w", stdout)
using namespace std;

int main(){
		FI;
        int t;
        cin>>t;
        for(int i=1; i<=t; i++){
            string s,tt;
            cin>>s;
            char check=s[0];
            tt=check;
            for(int j=1; j<s.length(); j++){
                check=tt[0];
                if(s[j]>=check){
                    tt.insert(0,1,s[j]);
                }
                else tt.insert(j,1,s[j]);
            }

            cout<<"Case #"<<i<<": "<<tt<<endl;
        }
    return 0;
}
