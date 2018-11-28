#include <bits/stdc++.h>

using namespace std;

int main(){

    int c;
    cin>>c;
    for(int i=0;i<c;i++){
        int n;
        cin>>n;
        int amigos=0, ov=0;
        for(int j=0;j<n+1;j++){
            char a;
            cin>>a;
            a-='0';
            if(ov<j){
                int b=j-ov;
                amigos+=b;
                ov+=b;


            }
            ov+=a;
        }

        cout<<"Case #"<<i+1<<": "<<amigos<<endl;
    }

    return 0;
}
