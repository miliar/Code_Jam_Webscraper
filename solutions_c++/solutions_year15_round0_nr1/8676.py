#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream f("test.in");
ofstream g("test.out");

int n,t;
string x;

void read(){

    f>>n>>x;
}

void solve(int c){

    g<<"Case #"<<c<<": ";
    int rez = 0,total_ppl = 0;
    for(int i=0;i<x.size();++i){

        if( i > total_ppl && x[i] != '0'){
            //cout<<"i:"<<i<<endl;
            rez += (i - total_ppl);
            total_ppl = i + x[i]-'0';
        }else
            total_ppl += x[i]-'0';
    }
    g<<rez<<"\n";
}

int main()
{
    f>>t;
    for(int i=1;i<=t;++i){
        read();
        solve(i);
    }
    return 0;
}
