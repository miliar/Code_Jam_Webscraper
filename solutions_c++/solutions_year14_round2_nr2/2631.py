#include<iostream>
#include<fstream>

using namespace std;

int main(){
    int caseN, i=1, j, k, temp;
    unsigned long A, B, K, countN;
    ifstream fin("B-small-attempt0.in");
	ofstream fout("namenum.out");
    fin>>caseN;
    while (i<=caseN){
        countN=0;
        fin>>A>>B>>K;
        for(j=0; j<A; j++){
            for(k=0; k<B; k++){
                temp=j&k;
                if (temp<K)
                    countN++;
            }
        }
        fout<<"Case #"<<i<<": "<<countN<<endl;
        i++;
    }
    return 0;
}
