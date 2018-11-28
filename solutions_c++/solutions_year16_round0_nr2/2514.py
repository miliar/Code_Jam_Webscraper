#include<bits/stdc++.h>
using namespace std;
#define ll long long int
ll genrate_fliping(string S , int i){

    ll counter =0;
        bool first =  true;
        for(int i=0;i<S.size();i++){
            if(first){
                while(S[i]=='-' && i<S.size()){
                    i++ , counter =1;
                }
                first = false;
            }
            if(S[i]=='-' && S[i-1]=='+')
                counter += 2;
        }
        return counter ;
}
int main(){

    ifstream cin("inp.in");
    ofstream cout("out.txt");
    int test;
    cin>>test;
    int i=1;
    while(test--){
        string S;
        cin>>S;
        cout<<"Case #"<<i<<": ";
        cout<<genrate_fliping(S , i)<<endl;
        i++;
    }
}
