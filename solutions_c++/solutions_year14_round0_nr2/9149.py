#include<iostream>
#include<list>
#include<cstdio>
#include<cmath>
#include<numeric>
#include<utility>
#include<list>
#include<set>
#include<map>
#include<bitset>
#include<vector>
#include<algorithm>
#include<bitset>
#include <deque>
#include<limits>
#include<string>
#include<cstring>
#include<cctype>
#include<iomanip>
#include<sstream>
#include<fstream>

using namespace std;

int main(){
	unsigned int T;
	cin >> T;

    for(int t = 1; t <= T; t++){
        double C, F, X;
        cin >> C >> F >> X;

        double prevans = X/2.0;
        if(X > C){
            double curans = 0.0;
            for(int f = 1;;f++){
                double c = 2.0;
                for(int h = 1; h <= f; h++){
                    curans += (C/c);
                    c += F;
                }
                curans += (X/c);
                if(curans >= prevans) break;
                else{ prevans = curans; curans = 0.0; }
            }
        }
        cout << fixed << setprecision(7) << "Case #" << t << ": " << prevans << endl;
    }
	return 0;
}
