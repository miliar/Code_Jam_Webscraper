#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("d1.in");
ofstream fout("d2.out");

int main(){
    int t;
    fin>>t;
    for(int j=0;j<t;j++){
        int k,c,s;
        fin>>k>>c>>s;
        fout<<"Case #"<<j+1<<": ";
        if((c==1)||(k==1)){
            for(int i=0;i<s;i++){
                fout<<i+1<<" ";
            }
        }
        else{
            for(int i=0;i<s;i++){
                fout<<i+2<<" ";
            }
        }
        fout<<endl;
    }
}
