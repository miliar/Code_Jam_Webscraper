#include <bits/stdc++.h>
#include <cstring>
using namespace std;
int main(){
    int T;
    cin>>T;
    string s;
    int frent,k=1;
    vector <char> word;
    while(T--){
        cin>>s;
        frent=-1;
        for(int i=0;i<s.length();i++){
            word.push_back(s[i]);
            if(s[i]>=frent){
                for(int j=word.size()-1;j>0;j--){
                    word[j]=word[j-1];
                }
                word[0]=s[i];
                frent=s[i];
            }
        }
        cout<<"Case #"<<k<<": ";
        for(int i=0;i<word.size();i++){
            cout<<word[i];
        }
        cout<<endl;
        word.clear();
        k++;
    }
    return 0;
}
