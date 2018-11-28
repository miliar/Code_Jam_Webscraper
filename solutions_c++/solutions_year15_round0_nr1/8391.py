#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input");
    fout.open("output");
    int T;
    fin>>T;
    for(int i=0;i<T;i++){
        int Smax;
        fin>>Smax;
        char c;
        int tmp;
        int add=0;
        int curr=0;
        for(int j=0;j<=Smax;j++){
            fin>>c;
            tmp=c-'0';
            if(tmp>0){
                if(curr>=j){
                    curr+=tmp;
                }
                else{
                    add+=j-curr;
                    curr=j+tmp;
                }
            }
        }
        fout<<"Case #"<<i+1<<": "<<add<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
