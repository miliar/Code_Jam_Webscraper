#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main(){
    int count,roll=0;
    cin>>count;
    while(count--){
        string t;
        cin>>t;
        int move=0;
        int start=0,end=t.length()-1;
        while(1){
            start=0;
            while(t[end]=='+' && end!=0){
                end--;
            }
            if(start==end){
                if(t[start]=='-') move++;
                break;
            }else{
                if(t[start]=='-'){
                    reverse(&t[0],&t[end+1]);
                    //cout<<"_1:"<<t<<endl;
                    for(int i=0;i<=end;i++){
                        t[i]=t[i]=='+'?'-':'+';
                    }
                    move++;
                    //cout<<"1:"<<t<<endl;
                    continue;
                }else{
                    while(t[start]=='+'){start++;}
                    for(int i=0;i<start;i++){
                        t[i]=t[i]=='+'?'-':'+';
                    }
                    move++;
                    //cout<<"2:"<<t<<endl;
                    continue;
                }
            }
        }

        cout<<"Case #"<<++roll<<": "<<move<<endl;
    }
}
