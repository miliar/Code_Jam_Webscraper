#include<iostream>
#include<fstream>
#include <stdlib.h>
using namespace std;


int main(){
    ifstream fin("A-small-attempt0");
    ofstream fout("ab.out");
    int t;
    fin>>t;
    for(int qq=1; qq<=t;qq++){
        unsigned long int temp, n,x;
        int i,count = 0;
        int a[10];
        for(int i=0; i<10;i++){
            a[i] = 0;
        }
        fin>>n;
        if(n==0){
            i=1000;
        }
        x = 0;
        for(int i=0; i<1000; i++){
            count = 0;
            x += n;
            temp = x;
            while(temp){
                a[temp%10] = 1;
                temp/=10;
            }
            for(int j=0;j<10;j++){
                if(a[j]){
                    count++;
                }else{
                    break;
                }
            }
            if(count==10){
                fout<<"Case #"<<qq<<": "<<x<<endl;
                break;
            }
        }
        if(count!=10){
            fout<<"Case #"<<qq<<": "<<"INSOMNIA"<<endl;
        }
    }
    return 0;
}