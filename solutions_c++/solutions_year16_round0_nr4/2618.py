#include<iostream>
#include<fstream>

using namespace std;

ifstream fin ("D-small-attempt0.in");
ofstream fout ("output.out");

long T,k,c,s;

int main(){
fin >> T;
for(int i=1;i<=T;i++){
    fin >> k >> c >> s;
    fout << "Case #" << i << ": ";
    fout << 1;
    for(int i=2;i<=k;i++)
        fout << " " << i;
    fout << endl;
}

}
