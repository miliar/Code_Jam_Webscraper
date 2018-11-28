#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main() {
    int n;
    ifstream in("A-small-attempt0.in");
    ofstream out("A-small-attempt0.out");
    in>>n;
    for(int i=0;i<n;i++) {
        vector <vector <int> >v1,v2;
        int n1,n2,count=0,value;
        in>>n1;
        n1--;
        v1.resize(4);
        v2.resize(4);
        for(int j=0;j<4;j++) {
            v1[j].resize(4);
            for(int k=0;k<4;k++)
                in>>v1[j][k];
        }
        in>>n2;
        n2--;
        for(int j=0;j<4;j++) {
            v2[j].resize(4);
            for(int k=0;k<4;k++)
                in>>v2[j][k];
        }
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                if (v1[n1][j] == v2[n2][k]) {count++; value=v1[n1][j]; }
        if (count == 0) out<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        else if (count == 1) out<<"Case #"<<i+1<<": "<<value<<endl;
        else out<<"Case #"<<i+1<<": Bad magician!"<<endl;
    }
}

