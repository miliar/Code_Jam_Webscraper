/*
* abeakkas
* Google CodeJam 2016 - Qualification
* Problem A
*/
#include <iostream>
#include <fstream>

typedef long long int ll;

#define pr pair<ll,ll>
#define vpr vector<pair<ll,ll> >

//(int *)calloc(1000000,sizeof(int));
//(int *)malloc(1000000*sizeof(int));

using namespace std; 
ifstream fin ("A.in");
ofstream fout ("A.out");

int digitify(int x, int digits) {
    while(x != 0) {
        digits |= 1 << (x % 10);
        x /= 10;
    }
    return digits;
}

int main(){
    int T;
    fin >> T;
    
    for(int iT = 1; iT <= T; iT++) {
        int N;
        fin >> N;
        if(N == 0) {
            fout << "Case #" << iT << ": INSOMNIA" << endl;
            continue;
        }
        int digits = 0;
        for(ll i = 1; i < 10000; i++) {
            digits = digitify(N * i, digits);
            if(digits == 1023) {
                fout << "Case #" << iT << ": " << N * i << endl;
                break;
            }
            //cout << N << " " << digits << endl;
        }
    }
	return 0;
}
