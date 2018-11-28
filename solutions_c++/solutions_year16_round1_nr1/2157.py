#include <iostream>
using namespace std;

int main(){
    freopen("readable.txt","w",stdout);
    int t;
    cin>>t;
    for (int ca=1;ca<=t;ca++){
        string s;
        cin>>s;
        string fin="";
        fin+=s[0];
        for (int i=1;i<s.size();i++){
            if (s[i]>=fin[0]) fin=s[i]+fin;
            else fin=fin+s[i];
        }
        cout<<"Case #"<<ca<<": "<<fin<<endl;
    }
    return 0;
}