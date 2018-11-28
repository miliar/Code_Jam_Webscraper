#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[]){
    int n;
    cin >> n;
    const int N = n;
    while(n--){
        const int MAX = 1000000;
        double C,F,X;
        cin >> C >> F >> X;
        vector<double> ttfn(MAX,0); //Time till farm N
        vector<double> ttdone(MAX,X/2.0);
        for(int i = 1; i < X; i++){
            ttfn[i] = ttfn[i-1] + C / (2.0 + (i-1)*F);
            ttdone[i] = ttfn[i] + X / (2 + F*i);
        }

        std::cout << "Case #"  << (N-n) << ": " << fixed << setprecision(15) << *min_element(ttdone.begin(),ttdone.end()) << std::endl;
    }
    return 0;
}