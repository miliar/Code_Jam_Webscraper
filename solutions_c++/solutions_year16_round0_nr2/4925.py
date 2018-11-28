#include<bits/stdc++.h>
using namespace std;


int getSolution(string S){
    S += "+";
    int out = 0;
    for(int i = 1; i<S.size();i++){
        if(S[i] != S[i-1]){
            out++;
        }
    }
    return out;
}

int main(){
    ifstream in;in.open("B-large.in");ofstream out("B-large.out");
    #define cin in
    #define cout out

    int T;
    cin>>T;
    for(int t =0;t<T;t++){
        string S;
        cin>>S;
        cout<<"Case #"<<(t+1)<<": ";
        cout<<getSolution(S)<<endl;
    }

}
