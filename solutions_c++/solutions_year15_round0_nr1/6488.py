#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
    int T;
    cin >> T;
    for(int i=1;i<=T;++i){
        int count;
        string s;
        vector<int> p;
        cin >> count;
        cin >> s;
        for(int j=0;j<=count;++j){
            p.push_back(s[j]-'0');
        }
        
        int invite=0, current =0;
        for(int j=0;j<=count;++j){
            if(current < j && p[j]){
                invite += j-current;
                current += j-current;
            }
            current += p[j];
//            cout << invite <<" "<< current<<endl;
        }
        cout << "Case #"<<i<<": " << invite<<endl;
    }
    return 0;
}