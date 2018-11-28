#include<bits/stdc++.h>
using namespace std;
int main(){
    int t;
    cin>>t;
            int x=1;
    while(t--){
        string s;
        int k;
        cin>>s;
        cin>>k;
        int i=0;
        int count=0;
        while(i<s.length()-k+1){
            if(s[i]=='-'){
                for(int j=0;j<k;++j){
                    if(s[i+j]=='-'){
                        s[i+j]='+';
                    }else{
                    s[i+j]='-';
                    }
                }
                count++;
            }
            ++i;
        } 
        bool con=true;
        for(i=s.length()-k;i<s.length();++i){
            if(s[i]=='-'){
                con=false;
                break;
            }
        }
        if(!con){
            cout<<"Case #"<<x++<<": "<<"IMPOSSIBLE"<<endl;
        }else{
        cout<<"Case #"<<x++<<": "<<count<<endl;
        }
    }
return 0;
}

