#include <bits/stdc++.h>

using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    ifstream cin("B-large.in");
    ofstream cout("largeOutput.txt");

    int tc, i, j, cont;
    string s;
    cin>>tc;
    j=1;
    while(j<=tc){
        cout<<"Case #"<<j<<": ";
        cin>>s;
        cont=0;

        for(i=1; i<s.size(); i++){
            if(s[i-1]!=s[i]){
                cont++;
            }
        }
        if(s[i-1]=='-'){
            cont++;
        }
        cout<<cont<<"\n";
        j++;
    }
    return 0;
}
