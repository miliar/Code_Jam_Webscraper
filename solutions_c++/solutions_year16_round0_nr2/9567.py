#include <bits/stdc++.h>
using namespace std;

int solve(string beg){
    bool minus = false;
    int cnt=0;
    for(int i=0; i<=(int)beg.size(); i++){
        if(beg[i]=='-'){
            if(!minus) cnt++, minus=true;
        }else{
            minus=false;
        }
    }
    return cnt*2-1+(beg[0]=='+');
}

int main(){
    
    int t;
    cin>>t;

    for(int tc=1; tc<=t; tc++){
        string cad;
        cin>>cad;
        cout<<"Case #"<<tc<<": "<<solve(cad)<<endl;
    }

    return 0;
}
