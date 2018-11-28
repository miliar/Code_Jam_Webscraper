#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;



int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        int N;
        cin >> N;
        vector<double> naomi(N);
        vector<double> ken(N);
        for(int i=0;i<N;i++) cin >> naomi[i];
        for(int i=0;i<N;i++) cin >> ken[i];
        
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        
        int war = N;
        int k = 0;
        for(int n=0;n<N&&k<N;n++){
            while(ken[k] < naomi[n] && k < N){
                k++;
            }
            if(k<N){
                war--; 
                k++;
            }
        }
        
        int dwar = 0;
        int n = 0;
        for(int k=0;k<N&&n<N;k++){
            while(naomi[n] < ken[k] && n < N){
                n++;
            }
            if(n<N){
                dwar++; 
                n++;
            }
        }
        
        cout << "Case #" << t << ": " << dwar << " " << war << endl;
        
        
    }

    return 0;
}