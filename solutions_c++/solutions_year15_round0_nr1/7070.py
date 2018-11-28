#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T,smax,fri,tmp;
    char ss;
    fin >> T;
    for (int t=1;t<=T;++t){
        fri = tmp = 0;
        fin >> smax;
        for (int i=0;i<=smax;++i){
            fin >> ss;
            if (tmp>=i)
                tmp += ss-'0';
            else{
                fri += i-tmp;
                tmp = i+ss-'0';
            }
        }
        fout << "Case #" << t << ": " << fri << endl;
    }
    return 0;
}
