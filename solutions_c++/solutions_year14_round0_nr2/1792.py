#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double t, c, f, x;
    cin>>t;
    double r=2, sp = 0;
    for(int k=1; k<=t; k++){
        cin>>c>>f>>x;
        sp = 0;
        r=2;
        if (x<c){   
            cout<< "Case #"<<k <<": "<<setprecision(10) << (x/r)<<"\n";
            continue;
        }
        while(true){
            if ((x/(r+f))>=((x-c)/r)){      //if upgrading would make it take more time
                cout<< "Case #"<<k <<": "<<setprecision(10) << sp + x/r<<"\n";
                break;
            }
            sp += c/r;
            r += f;
        }
    }
    return 0;
}
