#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("b.in");
ofstream fout("b2.out");

int main() {
int T;
fin>>T;
for(int z = 1; z <= T; z++) {
    int D, P[1001] = {0};
    int maxInd = 0;
    fin>>D;
    for(int i = 1; i <= D; i++) {
        int temp;
        fin>>temp;
        if(temp > maxInd) maxInd = temp;
        P[temp]++;
    }
    int ans = maxInd;
    for(int i = 1; i <= maxInd; i++) {
        int sum = 0;
        for(int j = 1; j <= maxInd; j++)
            sum += P[j]*(j/i -1 + ( (j%i == 0) ? 0 : 1) );
//        cout<<i<<' '<<sum<<' '<<endl;
        if(sum + i < ans) ans = sum+i;
    }
    fout<<"Case #"<<z<<": "<<ans<<endl;
//    system("pause");
}
}
