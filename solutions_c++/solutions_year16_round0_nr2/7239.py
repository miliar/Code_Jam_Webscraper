#include<iostream>
#include<fstream>
using namespace std;
int main(){
    ifstream iff("B-large.in");
ofstream off("code_jamB_large.txt");
int t,c=0;
iff>>t;
//cin>>t;
while(t--){
        c++;
    string str;
    iff>>str;
    bool flip = false;
    int count=0,cpos,len;
    len = str.length();
    cpos = len - 1;
    while(cpos>=0){
    if(!flip){
        while(cpos>=0 && str[cpos] == '+'){
            cpos--;
        }
    }else{
        while(cpos>=0 && str[cpos] == '-'){
            cpos--;
        }

    }
     flip=!flip;
     count++;

    }
    off<<"Case #" << c << ": "<<count - 1<<"\n";
}
return 0;
}
