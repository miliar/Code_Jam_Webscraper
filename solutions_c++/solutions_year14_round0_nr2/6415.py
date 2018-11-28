#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;
typedef vector<int> VI;

int main(){
    int nt;
    cin >> nt;
    for(int ct=1; ct<=nt; ++ct){
        double c, f, x, p=2, cookies=0, t=0;
        cin >> c >> f >> x;
        while(true){
            t += c/p;
            cookies = c;
            if((x-c)/p < x/(p+f)){
                t+=(x-c)/p;
                break;
            }
            else p+=f;
        }
        printf("Case #%d: %.7f\n", ct, t);
    }
}
