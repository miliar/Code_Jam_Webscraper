#include <iostream>
using namespace std;

int P[1000];
int D;

int main() {
    int T; cin>>T;
    for (int t=1; t<=T; t++) {
        
        cin>>D;
        for (int i=0; i<D; i++) cin>>P[i];
        
        int best = 1000;
        for (int c=1; c<=1000; c++) {
            int extra = 0;
            for (int i=0; i<D; i++)
                extra += (P[i]-1)/c;
            best = min(best, c+extra);
        }
        
        cout<<"Case #"<<t<<": "<<best<<endl;
    }
    

    return 0;
}
