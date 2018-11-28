#include<iostream>
#include <fstream>
using namespace std;


void calc(unsigned long long int x,bool num[10]){
    unsigned long long int t;
    
    while(x!=0){
        t = x % 10;
        x = x / 10;
        num[t] = true;
      //  cout<<t<<" made true "<<endl;
    }
    
}

bool check(bool num[10]){
    for(int i=0;i<10;i++){
        if(!num[i]){
            return false;
           // cout<<"Number "<<i<<" Still not found"<<endl;
        }
    }
    return true;
}
int main(){
    ifstream fin("sheepin.in");
    ofstream fout("sheepout.out");
    
    int t=0;
    unsigned long long n = 0;
    fin>>t;
    for(int a=1;a<=t;a++){
        bool c = false;
        bool num[10]={0};
        fin>>n;
        unsigned long long temp;
        for(int i=1;i<1000;i++){
            temp = n * i;
            calc(temp , num);
            if(check(num)){
                fout<<"Case #"<<a<<": "<<temp<<endl;
                c = true;
                break;
            }
        }
        if(!c){
        fout<<"Case #"<<a<<": INSOMNIA"<<endl;
        }
        
    }
    
    
    return 0;
}