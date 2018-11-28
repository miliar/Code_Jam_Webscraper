#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    double C,F,X;
    int CaseNums;
    ifstream fin("B-large.in");
	ofstream fout("namenum2.out");
    fin>>CaseNums;
    for(int i=1; i<=CaseNums; i++){
        double factor=2,ans=0;
        fin>>C>>F>>X;
        while(1){
            if(((C/factor)+(X/(factor+F)))<(X/factor)){
                    ans+=C/factor;
                    factor+=F;
            }
            else{
                ans+=X/factor;
                break;
            }
        }
        fout<<"Case #"<<i<<": "<<setprecision(7)<<fixed<<ans<<endl;
    }
    return 0;
}
