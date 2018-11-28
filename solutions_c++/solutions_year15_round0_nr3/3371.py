#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

//3rd question
char operate(char a, char b, bool &sign){
    if(a=='i'){
        if(b=='i'){
            if(sign==1){
                sign=0;
            }else{
                sign =1;
            }
            return 'x';
        }else if(b=='j'){
            return 'k';
        }else if(b=='k'){
            if(sign==1){
                sign = 0;
            }else
                sign = 1;
            return 'j';
        }
    }else if(a == 'j'){
        if(b=='i'){
            if(sign==1){
                sign=0;
            }else{
                sign =1;                
            }
            return 'k';
        }else if(b=='j'){
            if(sign==1){
                sign=0;
            }else{
                sign =1;                
            }
            return 'x';
        }else if(b=='k'){
            return 'i';
        }
        
    }else if(a=='k'){
        if(b=='i'){
            return 'j';
        }else if(b=='j'){
            if(sign==1){
                sign=0;
            }else{
                sign =1;                
            }
            return 'i';
        }else if(b=='k'){
            if(sign==1){
                sign=0;
            }else{
                sign =1;                
            }
            return 'x';
        }
    }else if(a=='x'){
        return b;
    }
    return 'x';
}

int main() {
    int t;
    string l;
    string lx;
    int x,size;
    char goi,goj,gok;
    int cases=1;
    int l1;
    cin>>t;
    while(t--){
        goi = 'x';
        goj = 'x';
        gok = 'x';
        cin>>l1>>x;
        cin>>l;
        lx = l;
        for(int i = 1;i<x;i++)
            lx+=l;
        size = lx.size();
        int i = 0;
        goi = 'x';
        bool sign = 0;
        
        while(goi!='i'&&i<size){
            goi = operate(goi,lx[i],sign);
            i++;
        }
        while(goj!='j'&&i<size){
            goj = operate(goj,lx[i],sign);
            i++;
        }
        while(i<size){
            gok = operate(gok,lx[i],sign);
            i++;
        }
        if(goi=='i'&&goj=='j'&&gok=='k'&&!sign){
            cout<<"Case #"<<cases<<": YES"<<endl;
        }else{
            cout<<"Case #"<<cases<<": NO"<<endl;
        }
        cases++;
    }
    return 0;
}


