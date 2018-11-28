#include <cmath>
#include <cstring>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
bool vowel(char a){
    int b=a;
    if((b=='a')||(b=='e')||(b=='i')||(b=='o')||(b=='u'))return true;
    else return false;}
int fun(string n,int a){
    int b=0;
    int ans=0;
    if(n.size()<a) return 0;
    for(int i=0;i<n.size();i++){
        if(vowel(n[i])){ b=0;}
        else{ b++;
             if(b == a){
                 ans=ans+((i-a+2)*(n.size()-i));
                // cout<<" "<<ans<<" ";
                        n.erase(n.begin(),n.begin()+i-a+2);
                        return ans+fun(n,a);}}}
    return 0;}

int main() {
    int t,a;
    cin>> t;
    //cout<<t;
    string w;
    getline(cin,w);
    //cout<<endl;
    for(int i=0;i<t;i++){
        string n;
        getline(cin,n);
        //cout<<n.size();
        //if((i == 0)||(i == t-1))n.erase(n.begin()+n.size()-1);
        a=0;
        for(int j=0;j<4;j++){
            int k=n[n.size()-1-j];
            if(k>= 48 && k<=57) a=a+(k-48)*pow(10,j);
            else{n.resize(n.size()-j-1);break;}}
        //cout<<n.size()<<" ";
        //cout<<a;
        int ans=fun(n,a);
        cout<<"Case #"<<i+1<<":"<<" "<<ans<<"\n";}
    return 0;
}
