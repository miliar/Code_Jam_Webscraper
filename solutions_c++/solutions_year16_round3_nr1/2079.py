#include <iostream>
#include <fstream>
using namespace std;

int main(){
    string file;
    cin >> file;
    ifstream in;
    in.open("c++/code_jam/A.in");
    ofstream out;
    out.open("c++/code_jam/politiikka");
    int T;
    in >> T;
    long summa=0;
    for (int t=1; t<=T; ++t){
        out << "Case #" << t << ": ";
        int n; in >> n;
        int z=1; while (z<n) z*=2;
        pair<int, int> d[2*z]={};
        for (int i=0; i<n; ++i){
            in >> d[z+i].first;
            summa +=d[z+i].first;
            d[z+i].second=i;
            int k=z+i;
            for (k/=2; k>=1; k/=2){
                d[k]=max(d[2*k], d[2*k+1]);
            }
        }
        while (d[1].first>0){
            int b=d[1].first;
            char a= 'A'+d[1].second;
            out << a;
            --d[z+d[1].second].first;
            --summa;
            int k=z+d[1].second;
            for (k/=2; k>=1; k/=2){
                d[k]=max(d[2*k], d[2*k+1]);
            }
            if (d[1].first==b && summa!=2){
                a='A'+d[1].second;
                k=z+d[1].second;
                out << a;
                --d[k].first; --summa;
                for (k/=2; k>=1; k/=2){
                    d[k]=max(d[2*k], d[2*k+1]);
                }
            }
            out << " ";
        }
        out << "\n";
    }
}
