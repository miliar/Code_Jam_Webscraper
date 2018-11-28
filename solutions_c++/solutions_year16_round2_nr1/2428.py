#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int tt;
    cin>>tt;
    for(int qq=1;qq<=tt;qq++){
        string s,tmp="";
        cin>>s;
        int ch[26]={0};
        cout<<"Case #"<<qq<<": ";
        for(char c: s){
            ch[c-'A']++;
        }
        while(ch['Z'-'A']!=0){
            ch['Z'-'A']--;
            ch['E'-'A']--;
            ch['R'-'A']--;
            ch['O'-'A']--;
            tmp+='0';
        }
        //cout<<tmp<<endl;
        while(ch['W'-'A']!=0){
            ch['T'-'A']--;
            ch['W'-'A']--;
            ch['O'-'A']--;
            tmp+='2';
        }
        //cout<<tmp<<endl;
        while(ch['U'-'A']!=0){
            ch['F'-'A']--;
            ch['O'-'A']--;
            ch['U'-'A']--;
            ch['R'-'A']--;
            tmp+='4';
        }
        //cout<<tmp<<endl;
        while(ch['X'-'A']!=0){
            ch['S'-'A']--;
            ch['I'-'A']--;
            ch['X'-'A']--;
            tmp+='6';
        }
        //cout<<tmp<<endl;
        while(ch['G'-'A']!=0){
            ch['E'-'A']--;
            ch['I'-'A']--;
            ch['G'-'A']--;
            ch['H'-'A']--;
            ch['T'-'A']--;
            tmp+='8';
        }
        //cout<<tmp<<endl;
        while(ch['O'-'A']!=0){
            ch['O'-'A']--;
            ch['N'-'A']--;
            ch['E'-'A']--;
            tmp+='1';
        }
        //cout<<tmp<<endl;
        while(ch['T'-'A']!=0){
            ch['T'-'A']--;
            ch['H'-'A']--;
            ch['R'-'A']--;
            ch['E'-'A']-=2;
            tmp+='3';
        }
        //cout<<tmp<<endl;
        while(ch['F'-'A']!=0){
            ch['F'-'A']--;
            ch['I'-'A']--;
            ch['V'-'A']--;
            ch['E'-'A']--;
            tmp+='5';
        }
        //cout<<tmp<<endl;
        while(ch['S'-'A']!=0){
            ch['S'-'A']--;
            ch['E'-'A']-=2;
            ch['V'-'A']--;
            ch['N'-'A']--;
            tmp+='7';
        }
        //cout<<tmp<<endl;
        while(ch['N'-'A']!=0){
            ch['N'-'A']--;
            ch['I'-'A']--;
            ch['N'-'A']--;
            ch['E'-'A']--;
            tmp+='9';
        }
        //cout<<tmp<<endl;
        sort(tmp.begin(),tmp.end());
        cout<<tmp<<endl;
    }
    return 0;
}
