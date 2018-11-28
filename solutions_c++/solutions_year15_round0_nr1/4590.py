#include <iostream>
#include <fstream>
#include <cstring>
#define LL long long
using namespace std;

LL T,S,a[2000]; char s[2000];

int main(){
    ifstream fin("input.in");
    ofstream fout("output.txt");
    fin >> T;

    int i,k; LL sum,res;
    for (k=1; k<=T; k++){
        fout << "Case #" << k << ": ";
        fin >> S >> s;
        for (i=0; i<=S; i++)
            a[i]=s[i]-'0';

        res=0,sum=a[0];
        for (i=1; i<=S; i++){
            if (a[i]==0) continue;
            if (i>sum)
                res+=(i-sum),sum=i;
            sum+=a[i];
        }

        fout << res << "\n";
    }
    return 0;
}
