#include<bits/stdc++.h>
using namespace std;
string digit[]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    int t;
    cin>>t;
    for(int z=1; z<=t; z++) {
        string s;
        cin>>s;
        map<char,int>mp;
        for(int i=0; i<(int)s.size(); i++) {
            mp[s[i]]++;
        }
        string ans="";
        while(mp['X']>0){
            ans+='6';
            for(int i=0;i<(int)digit[6].size();i++){
                mp[digit[6][i]]--;
            }
        }
        while(mp['Z']>0){
            ans+='0';
            for(int i=0;i<(int)digit[0].size();i++){
                mp[digit[0][i]]--;
            }
        }
        while(mp['U']>0){
            for(int i=0;i<(int)digit[4].size();i++){
                mp[digit[4][i]]--;
            }
            ans+='4';
        }
        while(mp['W']>0){
            for(int i=0;i<(int)digit[2].size();i++){
                mp[digit[2][i]]--;
            }
            ans+='2';
        }
        while(mp['G']>0){
            for(int i=0;i<(int)digit[8].size();i++){
                mp[digit[8][i]]--;
            }
            ans+='8';
        }
        while(mp['S']>0){
            for(int i=0;i<(int)digit[7].size();i++){
                mp[digit[7][i]]--;
            }
            ans+='7';
        }
        while(mp['V']>0){
            for(int i=0;i<(int)digit[5].size();i++){
                mp[digit[5][i]]--;
            }
            ans+='5';
        }
        while(mp['I']>0){
            for(int i=0;i<(int)digit[9].size();i++){
                mp[digit[9][i]]--;
            }
            ans+='9';
        }
        while(mp['R']>0){
            for(int i=0;i<(int)digit[3].size();i++){
                mp[digit[3][i]]--;
            }
            ans+='3';
        }
        while(mp['O']>0){
            for(int i=0;i<(int)digit[1].size();i++){
                mp[digit[1][i]]--;
            }
            ans+='1';
        }
        sort(ans.begin(),ans.end());
        cout<<"Case #"<<z<<": "<<ans<<"\n";
    }
    return 0;
}
