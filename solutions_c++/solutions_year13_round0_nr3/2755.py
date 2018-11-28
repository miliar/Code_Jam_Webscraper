#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
//#include <vector>
//#include <algorithm>
//#include <cassert>
using namespace std;
int N;
        int A,B;
bool isPal(int i)
{
    int digits=(int)ceil(log(i)/log(10));
    int pow=1;for(int x=1;x<digits;x++) pow*=10;//pow=10^(digits-1)
    for(int j=1;j*2<=digits;j++)
    {
        if((i/pow)!=(i%10)) return false;
        else{
            i%=pow;
            i/=10;
            pow/=100;
        }
    }
    return true;
}
int main() {
    std::ifstream fin ("C-small.in");
    std::ofstream fout("fair.out");
    fin>>N;
    //for(int i=0;i<200;i++) if(isPal(i)) cout<<i<<"\t";
    for(int i=0;i<N;i++)
    {
        fout<<"Case #"<<(i+1)<<": ";
        fin>>A>>B;
        int num=0;
        for(int n=0;n*n<=B;n++){
            if(n*n<A) continue;
            if(isPal(n) && isPal(n*n)) num++;
        }
        fout<<num<<"\n";
    }
    
    return 0;
}
