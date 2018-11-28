#include<iostream>
#include<string>
using namespace std;

int findLast(string str){
    int last = -1;
    for(int i=str.length() - 1 ; i >= 0;i--){
        if(str[i] == '-'){
            last = i;
            break;
        }
    }

    return last;
}

string flip(string str,int to){
    for(int i=0;i<=to;i++){
        if(str[i] == '-'){
            str[i] = '+';
        }else{
            str[i] = '-';
        }
    }
    return str;
}

int main(){

    int t;
    int x=1;
    cin>>t;
    while(x<=t){

    string str;
    cin>>str;

    int flips=0;

    while(1){
        int last = findLast(str);
        if(last == -1){
           break;
        }
        str = flip(str,last);
        flips++;
    }

    cout<<"Case #"<<x<<": "<<flips<<endl;
    x++;
    }
}
