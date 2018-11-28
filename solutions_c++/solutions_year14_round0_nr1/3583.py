#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
using namespace std;

int main(void){

    ifstream fin("A-small.in");
    ofstream fout("A-small.out");
    int n;
    fin>>n;
    int a[16],b[16];
    int first,second;
    for(int t = 1; t <= n; t++){
        int one[4];
        int two[4];
        fin>>first;
        for ( int i = 0; i < 16; i++ )
            fin>>a[i];
        fin>>second;
        for ( int i = 0; i < 16; i++ )
            fin>>b[i];
        int start = (first-1) * 4;
        for ( int i = 0; i < 4; i++ )
            one[i] = a[start+i];
        start = (second-1) * 4;
        for ( int i = 0; i < 4; i++ )
            two[i] = b[start+i];
        int check = 0;
        int ans = 0;
        for ( int i = 0; i < 4; i++ ){
            for ( int j = 0; j < 4; j++ ){
                if ( one[i] == two[j] ){
                    ++check;
                    ans = one[i];
                }
            }
        }
        fout<<"Case #"<<t<<": ";
        if ( check == 0 )
            fout<<"Volunteer cheated!"<<"\n";
        else
        if ( check == 1 )
            fout<<ans<<"\n";
        else
            fout<<"Bad magician!"<<"\n";
    }
    return 0;
}

