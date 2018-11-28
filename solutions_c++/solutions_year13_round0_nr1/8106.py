#include <iostream>
#include <vector>
using namespace std;

inline void check(vector<string> &v){
    char c=0;
    bool b=true;
    for(int i=0;i<4;++i){
        b=true;
        for(int j=0;j<3;++j){
            if(v[i][j]=='.' || v[i][j+1]=='.'){
                b=false;
                break;
            }
            if((c?v[i][j+1]==c || (v[i][j+1]=='T'&&v[i][j]==c):v[i][j]==v[i][j+1]||v[i][j]=='T'||v[i][j+1]=='T')){
               if(!c)c=(v[i][j]=='T'?v[i][j+1]:v[i][j]);
            }
            else {
                b=false;
                break;
            }
        }
        if(b){
            cout<<c<<" won\n";
            break;
        }
        b=true,c=0;
        for(int j=0;j<3;++j){
            if(v[j][i]=='.' || v[j+1][i]=='.'){
                b=false;
                break;
            }
            if((c?v[j+1][i]==c || (v[j+1][i]=='T'&&v[j][i]==c):v[j][i]==v[j+1][i]||v[j][i]=='T'||v[j+1][i]=='T')){
                if(!c)c=(v[j][i]=='T'?v[j+1][i]:v[j][i]);
            }
            else {
                b=false; break;
            }
        }
        if(b){
            cout<<c<<" won\n";
            break;
        }
    }
    if(b)return;
    b=true,c=0;
    for(int i=0;i<3;++i){
        if(v[i][i]=='.' || v[i+1][i+1]=='.'){
                b=false;
                break;
        }
        if((c?v[i+1][i+1]==c || (v[i+1][i+1]=='T'&&v[i][i]==c):v[i][i]==v[i+1][i+1]||v[i][i]=='T'||v[i+1][i+1]=='T')){
            if(!c)c=(v[i][i]=='T'?v[i+1][i+1]:v[i][i]);
        }
        else {
            b=false; break;
        }
    }
    if(b){
        cout<<c<<" won\n";
        return;
    }
    b=true,c=0;
    for(int i=3;i>0;--i){
        if(v[i][3-i]=='.' || v[i-1][4-i]=='.'){
                b=false;
                break;
        }
        if((c?v[i-1][4-i]==c || (v[i-1][4-i]=='T'&&v[i][3-i]==c):v[i][3-i]==v[i-1][4-i]||v[i][3-i]=='T'||v[i-1][4-i]=='T')){
            if(!c)c=(v[i][3-i]=='T'?v[i-1][4-i]:v[i][3-i]);
        }
        else {
            b=false; break;
        }
    }
    if(b){
        cout<<c<<" won\n";
        return;
    }
    b=true,c=0;
    for(int i=0;i<4 && b;++i)
        for(int j=0;j<4 && b;++j)
            if(v[i][j]=='.')b=false;
    if(b)cout<<"Draw\n";
    else cout<<"Game has not completed\n";
}

int main(){
    vector<string> v(4);
    int n;
    cin>>n;
    for(int t=1;t<=n;++t){
        for(int i=0;i<4;++i)cin>>v[i];
        cout<<"Case #"<<t<<": ";
        check(v);
        cin.get();
    }
    return 0;
}
    
