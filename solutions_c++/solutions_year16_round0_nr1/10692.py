#include<fstream>
#include<iostream>
using namespace std;
bool isFlag(int x[]){
    for(int i = 0;i < 10;i++){
        if(x[i] == 0){
            return false;
        }
    }
    return true;
}
int check(int x){
    int flag[10] = {0},t,i = 2;
    while(!isFlag(flag)){
        t = x;
        while(x){
            flag[x%10] = 1;
            x = x/10;
        }
        x = i*x;
        i++;
    }
    return t;
}
int main(){
    ifstream fin;
    ofstream fout;
    char ct,cn;
    int in;
    fin.open("t.txt");
    fout.open("r.txt");
    fin>>ct;
    int it = ct - '0';
    for(int i = 1;i <= it;i++){
        fin>>cn;
        in = cn - '0';
        if(in == 0){
            fout<<"Case #"<<i<<": INSOMNIA"<<endl;
        }
        else{
            int l = check(in);
            fout<<"Case #"<<i<<": "<<l<<endl;
        }
    }
    return 0;
}
