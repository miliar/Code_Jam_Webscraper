#include<vector>
#include<algorithm>
#include<tuple>
#include<iostream>
#include<fstream>
#include<string>
#define LLI long long int
using namespace std;

int main(){
    int T, N;
    ifstream fin("A-large.in");
    ofstream fout("res.txt");
    fin>>T;
    //cout<<T<<endl;
    N = T;
    while(T--){
        int smax;
        char * str;
        fin>>smax;
        str = new char[smax+1];
        fin>>str;
        //cout<<smax<<endl;
        //cout<<str<<endl;
        int inv = 0, tot = 0;
        for(int i = 0; i <= smax; i++){
            if(tot < i){
                inv++;
                tot++;
            }
            tot += (int)str[i] - 48;
        }
        fout<<"Case #"<<(N-T)<<": "<<inv<<endl;
    }
    fin.close();
    fout.close();
}
