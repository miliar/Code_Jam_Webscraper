#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    int t;
    cin>>t;
    string s;
    int cases = 1;
    int f;
    int temp;
    int res;
    int l;
    while(t--){
        cin>>l;
        cin>>s;
        res = 0;
        temp = 0;
        for(int i = 0;i<s.size();i++){
            f = s[i]-'0';
            if(i>temp){
                res = res+i-temp;
                temp = i+f;
            }else{
                temp +=f;
            }
        }
        cout<<"Case #"<<cases<<": "<<res<<endl;
        cases++;
    }
    
    
    return 0;
}
