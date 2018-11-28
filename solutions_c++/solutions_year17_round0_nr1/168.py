#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int tc,k;
string str;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>tc;
    for(int ct=1;ct<=tc;++ct){
        cin>>str>>k;
        int uses=0;
        bool good=true;
        for(int i=0;i<=(int)str.size()-k;++i){
            if(str[i]=='-'){
                for_each(str.begin()+i,str.begin()+i+k,[](char& c){
                    if(c=='-'){
                        c='+';
                    }
                    else{
                        c='-';
                    }
                });
                ++uses;
            }
        }
        for(int i=(int)str.size()-k+1;i<(int)str.size();++i){
            if(str[i]=='-'){
                good=false;
                break;
            }
        }
        if(good){
            cout<<"Case #"<<ct<<": "<<uses<<endl;
        }
        else{
            cout<<"Case #"<<ct<<": IMPOSSIBLE"<<endl;
        }
    }
}
