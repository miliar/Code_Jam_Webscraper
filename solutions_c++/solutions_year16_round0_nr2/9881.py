#include <iostream>
#include <string>

using namespace std;

int main(){
    string s;
    int t;
    cin>>t;
    for(int x=0;x<t;x++){
        cin>>s;
        char c=s[0];
        int sol=0;
        for(int i=1;i<s.length();i++){
            if(s[i]!=c){
                sol++;
                c=s[i];
            }   
        }
        if(c=='-'){
            sol++;
        }
        cout<<"Case #"<<x+1<<": "<<sol<<endl;
    }
    return 0;
}
