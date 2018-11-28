#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("al.in");
ofstream fout("al.out");

int main(){
    int t;
    fin>>t;
    for(int j=0;j<t;j++){
        string a;
        fin>>a;
        string f="";
        f+=a[0];
        for(int i=1;i<a.length();i++){
            if(a[i]>=f[0]){
                f=a[i]+f;
            }
            else{
                f+=a[i];
            }
        }
        fout<<"Case #"<<j+1<<": "<<f<<endl;
    }
}
