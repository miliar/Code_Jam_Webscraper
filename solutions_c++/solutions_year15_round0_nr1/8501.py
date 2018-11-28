#include <iostream>
#include <string>

using namespace std;

int main(){
    string s;
    int T;
    cin>>T;
    for(int i = 1; i<=T; i++){
        int max_shyness;
        cin>>max_shyness;
        cin>>s;
        int needed = 0;
        int current = 0;
        if(s.size() <= 1){
            cout<<"Case #"<<i<<": "<<needed<<endl;
        } else {
            for(int i = 0; i < max_shyness + 1; i++){
                if(current < i) {
                    int friends_needed = i-current;
                    current += friends_needed;
                    needed += friends_needed;
                }
                current += (s[i] -'0');
            }
            cout<<"Case #"<<i<<": "<<needed<<endl;
        }
    }
}
