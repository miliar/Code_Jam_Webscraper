#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){

    ifstream cin("inp.in");
    ofstream cout("out.txt");
    int t;
    cin>>t;
    int i=1;
    while(t--){
        string S;
        cin>>S;
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
        cout<<"Case #"<<i++<<": ";
        cout<<counter<<endl;
    }

}
