#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    ifstream fin("B-large.in");
    ofstream fout("output.txt");
int t;
fin>>t;
int j=1;
while(t--){
    string s;
    fin>>s;
    int count=0;
    int flag=0;
    for(int i=0;i<s.size();i++){
            if(s[i]=='-' && flag==0){
                count=1;
            }
        if(s[i]=='+' && flag==0){
                if(i-1>=0){
                    if(s[i-1]=='-'){
                        count=1;
                    }
                }
            flag=1;
        }
        if(s[i]=='-' && flag==1){
            if(s[i-1]=='-'){
                    continue;
            }
            else if(s[i-1]=='+'){
                count+=2;
            }
        }
    }
    fout<<"Case #"<<j<<": "<<count<<endl;
    j++;
}
}
