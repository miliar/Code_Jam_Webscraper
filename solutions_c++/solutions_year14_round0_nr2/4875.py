#include <iostream>
#include <sstream>
#include <cstdio>

using namespace std;

int main(){
int t;
int i,k,p;
double time_buy[10000];
double c, f, x;
double my_c;
double ans;

    cin >> t;
    for (i = 1; i <= t; i++){
        scanf("%Lf", &c);
        scanf("%Lf", &f);
        scanf("%Lf", &x);

        my_c = 2.0;
        ans = 0.0;

    k = 1;
    while (k){
        time_buy[k] = c/my_c;

        if (((time_buy[k])+(x/(my_c+f))) >= (x/my_c)){
           for (p = 1; p < k; p++){
                ans += time_buy[p];
            }
            ans += x/my_c;
            break;
        }
        my_c += f;
        k++;
    }

     cout << "Case #" << i << ": ";
     printf("%Lf", ans);
     cout << endl;
    }


    return 0;
}
