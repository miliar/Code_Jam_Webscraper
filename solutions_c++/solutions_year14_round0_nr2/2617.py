#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
    freopen("t.txt","r",stdin);
    freopen("o.txt","w",stdout);
    int T;
    double C,F,X,total,growth;
    cin >> T;
    C=435;
    F=3;
    X=1039;
    for(int t=0;t<T;t++){
        cin >> C >> F >> X;
        total=0;
        growth=2;
        while(true){
                //cout << total << endl;
            if(X/growth < C/growth + X/(growth+F)){
                total=total+X/growth;
                break;
            }
            total=total+C/growth;
            growth=growth+F;
        }

        printf("Case #%i: %.7lf\n",t+1,total,C,F,X);
    }
    return 0;
}
