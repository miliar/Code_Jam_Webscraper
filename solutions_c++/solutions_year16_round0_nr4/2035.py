#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

unsigned long long int macht(int a,int b){
    unsigned long long int ans=1;
    for(int i=0;i<b;i++){
        ans*=a;
    }
    return ans;
}

int main (){
    ifstream in("Dl.in");
    ofstream out("dloutput.txt");
    int testcases;
    in >> testcases;
    int testcasses = testcases;
    while (testcasses -->0){
        int K,C,S;
        in>>K>>C>>S;
        if(C*S<K){
            out<<"Case #"<<testcases-testcasses<<": IMPOSSIBLE"<<endl;continue;
        }
        bool kapermaarmee=false;
        long long int i=0;
        out<<"Case #"<<testcases-testcasses<<":";
        while(!kapermaarmee){
            unsigned long long int opl=0;
            for(int j=0;j<C;j++){
                if(i<K){
                    opl+=i*macht(K,j);
                    i++;
                    continue;
                }
                kapermaarmee=true;
            }
            if(i==K)kapermaarmee=true;
            out<<" "<<opl+1;
        }
        out<<endl;
    }
    return 0;
}
