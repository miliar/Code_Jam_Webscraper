#include <bits/stdc++.h>

using namespace std;

void flip(string &t,int i){
    for(;i>=0;i--){
        if(t[i]=='+'){
            t[i]='-';
        }
        else{
            t[i]='+';
        }
    }
}

int main(){

    int t;
    cin>>t;
    for (int i=1;i<=t;i++){
        string t;
        cin>>t;
        int count=0;
        for(int j=t.length()-1;j>=0;j--){
            if(t[j]=='-'){
                flip(t,j);
                count++;
            }
        }
        cout<<"Case #"<<i<<": "<<count<<endl;
    }
return 0;
}