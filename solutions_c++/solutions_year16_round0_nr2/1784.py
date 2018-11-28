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
#include <string>

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
ifstream fin ("B.in");
ofstream fout ("B.out");

int main(){
    int T;
    fin>>T;
        string str;
        getline(fin, str);
    for(int iT = 1; iT <= T; iT++){
        getline(fin, str);
        int n = 0;
        for(int i = 0; i < str.length() - 1; i++) {
            n += str[i] != str[i + 1];
        }
        n += str[str.length() - 1] == '-';
        fout << "Case #" << iT << ": " << n << endl;
    }
	return 0;
}
