#include <iostream>
#include <bits/stdc++.h>


using namespace std;

int tryy(string str){
    int v=0;
    bool z=true;
    for(int i=0;i<str.length();i++){
        if(str[i]=='-')z=false;
    }
    while(!z){
        int pos=str.length()-1;
        while(str[pos]!='-'){
            pos--;
        }
        for(int i=0;i<=pos;i++){
            if(str[i]=='+')str[i]='-';
            else if(str[i]=='-')str[i]='+';
        }
        v++;
        z=true;
        for(int i=0;i<str.length();i++){
            if(str[i]=='-')z=false;
        }
    }
    return v;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    cin>>t;
    int a[t];
    for(int i=0;i<t;i++){
        string tmp;
        cin>>tmp;
        a[i]=tryy(tmp);
    }
    for(int i=0;i<t;i++){
        cout<<"Case #"<<i+1<<": "<<a[i]<<endl;
    }
}
