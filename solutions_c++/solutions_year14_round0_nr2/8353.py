#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <bitset>
#include <cstring>
#include <vector>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        double C,F,X,rate=2.0,time=0;
        int current=0;
        cin >> C >> F >> X;
        while(current<X){
            if(X/rate > C/rate + X/(rate+F)){
                time+=C/rate;
                rate+=F;
            }
            else{
                time+=X/rate;
                break;
            }
        }
        printf("Case #%d: %.7lf\n",t+1,time);
    }
}
