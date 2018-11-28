#include <iostream>
#include <string>
#include <cstdio>
#include <climits>
using namespace std;

pair<bool,char> multi(char x,char y){
    pair<bool,char> res;
    if (x=='1'){
        res.first=false;
        res.second=y;
    }
    else if (y=='1'){
        res.first=false;
        res.second=x;
    }
    else if (x==y){
        res.first=true;
        res.second='1';
    }
    else{
        if ( (x-'i'+1)%3==(y-'i')%3 ){
            res.first=false;
        }
        else{
            res.first=true;
        }
        res.second='i'+'j'+'k'-x-y;
        
    }
    
    return res;
}

int main(){
    //getResult("jijiji");
    //getResult("");
    freopen("/Users/jiangzefan/code/C/C/input.txt","r",stdin);
    freopen("/Users/jiangzefan/code/C/C/output.txt","w",stdout);
    int _,__;
    scanf("%d",&_);
    for (__=1;__<=_;__++){
        int L,X;
        cin >> L >> X;
        string s;
        cin >> s;
        string t;
        for (int i=0;i<X;i++){
            t.append(s);
        }
        
        bool flag=false;
        char ch='1';
        int p=-1,q=-1;
        for (int i=0;i<t.size();i++){
            pair<bool,char> res=multi(ch, t[i]);
            flag^=res.first;
            ch=res.second;
            if (!flag && ch=='i' && p<0){
                p=i;
            }
            if (!flag && ch=='k'){
                q=i;
            }
        }
        bool ans = 0<=p && p<q && flag && ch=='1';
        
        printf("Case #%d: %s\n",__,ans?"YES":"NO");
    }
    
}