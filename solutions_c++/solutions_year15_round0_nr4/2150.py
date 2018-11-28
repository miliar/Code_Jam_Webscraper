#include <iostream>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <iterator>
#include <string>
#include <fstream>

using namespace std;

typedef long long int64;

#define mp make_pair
#define pb push_back
#define ms0(x) memset(x,0,sizeof(x));
#define ms1(x) memset(x,-1,sizeof(x));

#define mod 1
#define EPS 1e-8

//------------------------------------------------------------------------//

int main(){
    ifstream fin;
    ofstream fout;

    fin.open("in.txt");
    fout.open("out.txt");

    int tst;
    fin >> tst;

    for(int t=1;t<=tst;t++){
        int x,r,c;
        fin >> x >> r >> c;
        fout << "Case #" << t << ": ";
        if(x==1){
            fout << "GABRIEL" << endl;
        }else if(x==2){
            if(r%2==0 || c%2==0) fout << "GABRIEL" << endl;
            else fout << "RICHARD" << endl;
        }else if(x==3){
            if((r==2 && c==3) || (r==3 && c==2) || (r==3 && c==3) || (r==3 && c==4) || (r==4 && c==3)){
                fout << "GABRIEL" << endl;
            }else fout << "RICHARD" << endl;
        }else if(x==4){
            if((r==3 && c==4) || (r==4 && c==3) || (r==4 && c==4)){
                fout << "GABRIEL" << endl;
            }else fout << "RICHARD" << endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}
