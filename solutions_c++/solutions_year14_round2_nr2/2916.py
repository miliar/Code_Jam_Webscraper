#include<fstream>
#include<iostream>

using namespace std;

int main() {
    int T,A,B,K;
    long long ans=0;
    ifstream readinput;
    ofstream writeoutput;
    writeoutput.open("output1B_b_small.txt",ios::out);
    readinput.open("B-small-attempt0.in",ios::in);
    readinput>>T;
    for(int i=1;i<=T;i++) {
        readinput>>A;
        readinput>>B;
        readinput>>K;
        for(int j=0;j<A;j++) {
            for(int l=0;l<B;l++) {
                int t1=j,t2=l;
                if((t1&t2)<K) {
                    ans++;  
                }
            }
        }
        writeoutput<<"Case #"<<i<<": "<<ans<<endl;
        ans=0;
    }
    return 0;
}
