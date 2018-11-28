#include <iostream>
#include <string>
using namespace std;

int main(){
    int t;
    cin>>t;
    
    for(int i = 0; i<t; i++){
        cout<<"Case #"<<i+1<<": ";
        
        string s;
        cin>>s;
        int count = 0;
        for(int j = 0; j<s.length()-1; j++){
            if(s[j] != s[j+1])
                count++;
        }
        if(s[s.length()-1] == '-')
            count++;
        cout<<count<<endl;
    }
    return 0;
}