
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <iomanip>
using namespace std;

int max(int a,int b){
    return a < b ? b : a;
}
int min(int a,int b){
    return a > b ? b : a;
}


double solve(double C,double F,double X){

    vector<double> spendtime;
    
    int i=0;
    int flg=0;
    while(flg==0){

        if((double)X/(double)(2+F*(i+1))+((double)C/(double)(2+F*i))>=(double)X/(double)(2+F*i) || C*(i+1)>=X){
            break;
        }
        spendtime.push_back((double)C/(double)(2+F*i));
        i++;
    }
    
    double ans=0;
    for(int i=0;i<spendtime.size();i++){
        ans = ans + spendtime[i];
    }
    ans = (double)ans + (double)X/(double)(2+F*i);

    return ans;
}


int main(int argc, const char * argv[])
{
    //CodeJam *codejam;
    
    std::ifstream ifs( "a.txt" );
    
    int T;
    ifs >> T;
    int t=1;
    while(t<=T){
        double C,F,X;
        ifs >> C >> F >> X;
        
        double ret = solve(C,F,X);
        
        cout.setf(std::ios_base::fixed,std::ios_base::floatfield);
        std::cout << "Case #" << t << ": " << setprecision(7) << ret << std::endl;
        t++;
    }
    return 0;
    
}

