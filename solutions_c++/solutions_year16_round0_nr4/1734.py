/*
* abeakkas
* Google CodeJam 2014 - Round 2
* Problem A
* Game after game after game...
*/
#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <utility>

typedef long long int ll;

#define pr pair<ll,ll>
#define vpr vector<pair<ll,ll> >

//DEBUGGING
#define _s cout<<
#define _d <<" "<<
#define _e <<endl;

//(int *)calloc(1000000,sizeof(int));
//(int *)malloc(1000000*sizeof(int));

using namespace std; 
ifstream fin ("D.in");
ofstream fout ("D.out");

int main(){
    int T;
    fin >> T;
    for(int iT=1;iT<=T;iT++) {
        int K, C, S;
        fin >> K >> C >> S;
        fout<<"Case #"<<iT<<":";
        // Easy isn't it :)
        for(int i = 1; i <= S; i++) {
            fout << " " << i;
        }
        fout << endl;
    }
	return 0;
}
