#include <iostream>
#include <fstream>

using namespace std;

int main(){
    int T;
    ifstream din;
    ofstream dout;

    din.open("D-small-attempt0.in", ifstream::in);
    dout.open("D-small-attempt0.out", ofstream::out);

    din>>T;
    cout<<T<<endl;
    din.ignore();
    for(int t=1; t<=T; t++){
        long K, C, S;
        din>>K>>C>>S;
        dout<<"Case #"<<t<<":";
        if(K==S){
            for(long s=1; s<=S; s++)
                dout<<" "<<s;
        }
        dout<<endl;
    }

    din.close();
    dout.clear();
    return 0;
}
