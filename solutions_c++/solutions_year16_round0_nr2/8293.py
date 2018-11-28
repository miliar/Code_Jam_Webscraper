#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream input("input.txt");
    ofstream output("output.txt");
    string stringa;
    unsigned long long n;
    input >> n;
    for(unsigned long long j=0;j<n;j++){
        input >> stringa;
        unsigned long long l=stringa.size();
        bool s[l];
        for(unsigned long long i=0;i<l;i++){
            if(stringa[i]=='-')
                s[i]=0;
            else
                s[i]=1;
        }
        bool actual=s[0];
        unsigned long long times=0;
        if(s[l-1]==0)
            times++;
        for(unsigned long long i=1;i<l;i++){
            if(s[i]!=actual){
                actual=s[i];
                times++;
            }
        }
        output << "Case #" << j+1 << ": "<< times << endl;
    }
    return 0;

}
