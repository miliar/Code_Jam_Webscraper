#include <fstream>
#include <iostream>
using namespace std;

int main()
{
    ifstream fin("magician.in");
    ofstream fout("magician.out");
    
    int t; fin >> t;
    for(int i=0; i<t; ++i) {
        fout << "Case #" << i+1 << ": ";
        int a; fin >> a;
        int line[4];
        for(int j=0; j<4; ++j) {
            int p,q,r,s; fin >> p >> q >> r >> s;
            if(j==a-1) {line[0]=p; line[1]=q; line[2]=r; line[3]=s;}
        }
        int b; fin >> b;
        int line2[4];
        for(int j=0; j<4; ++j) {
            int p,q,r,s; fin >> p >> q >> r >> s;
            if(j==b-1) {line2[0]=p; line2[1]=q; line2[2]=r; line2[3]=s;}
        }
        
        int same=0;
        int x;
        for(int j=0; j<4; ++j) for(int k=0; k<4; ++k) {
            if(line[j] == line2[k]) {++same; x=line[j];}
        }
        if(same==0) fout << "Volunteer cheated!\n";
        else if(same==1) fout << x << endl;
        else fout << "Bad magician!\n";
    }
}
