#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>
using namespace std;
int main(){
    int t;
    int tt=1;

    ifstream fin("InputFile.txt");
    ofstream fout("output.txt");

 fin>>t;
  char A[2001];
    int l;
    while(t--){
        fin>>l>>A;
        int i=0;
        int f=0;
        int s=0;
        while(i<=l){
            if(s>=i){
                s+=(A[i]-48);
            }
            else{
                f+=(i-s);
                s+=(i-s);
                s+=(A[i]-48);
            }
            i++;
        }
        fout<<"Case #"<<tt<<": "<<f<<"\n";
        tt++;
    }
    fin.close();
    fout.close();
    return 0;
}

