#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

vector<double> N,K;

int main (){
    ifstream fin("D-large.in");
    ofstream fout("D-large.out");
    int t,n,war,dwar,i,j; fin>>t;
    for (int cpt=1;cpt<=t;++cpt){
        fin>>n;
        N.resize(n);K.resize(n);
        for (i=0;i<n;++i) fin>>N[i]; sort(N.begin(),N.end());
        for (i=0;i<n;++i) fin>>K[i]; sort(K.begin(),K.end());
        i=0,j=0,war=0;
        while (j<n) if (N[i]<K[j]) i++,j++; else j++,war++;
        i=n-1,j=n-1,dwar=0;
        while (j>=0) if (N[i]>K[j]) dwar++,i--,j--; else j--;
        fout<<"Case #"<<cpt<<": "<<dwar<<" "<<war<<endl;
    }
    return 0;
}
