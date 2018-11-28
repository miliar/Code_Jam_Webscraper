#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("outputLarge.txt");

    int T, n, m[1000], d, dm, x;

    fin >> T;
    for(int i = 0; i < T; i++){
            fin >> n;
            for(int j = 0; j < n; j++){
                fin >> m[j];
            }
            x = 0;
            for(int k = 1; k < n; k++){
                d = m[k-1] - m[k];
                if(d > 0) x += d;
            }
            fout<<"CASE #"<<i+1<<": "<<x<<" ";
            x = 0;
            dm = 0;
            for(int p = 1; p < n; p++){
                if((m[p-1] - m[p]) > dm) dm = (m[p-1] - m[p]);
            }
            for(int l = 1; l < n; l++){
                d = m[l-1] - m[l];
                    if(m[l-1] >= dm){
                        x += dm;
                    }
                    else x += m[l-1];
            }
            fout<<x<<"\n";
    }

    return 0;
}
