#include <iostream>
#include <string>
using namespace std;

int main(){
    int T;         cin>>T;
    for(int i=1; i<=T; ++i){
        string s;   cin>>s;
        char a=s[0];
        int l = s.length();
        
        int count = 0;
        for(int j=1; j<l; ++j){
            if(s[j]!=s[j-1]){
                if(a=='-')  a='+';
                else        a='-';
                count++;
            }
        }
        if(a=='-')
            count++;
        
        cout<<"Case #"<<i<<": "<<count<<endl;
    }
    
    return 0;
}
