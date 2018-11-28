#include <iostream>
#include <string>
#include <cmath>
using namespace std;

string s; 
const int MAXN = 4; 
char ch; 
int tests, test, n, m, x, y;
double C, F, X; 

int main(){
    freopen("2.in","r",stdin); 
    freopen("2.out","w",stdout);

    scanf("%d",&tests);
    
    for (test = 1; test <= tests; ++test){
        scanf("%lf %lf %lf", &C, &F, &X); 
        
        double money = 0, ans = 0, v = 2.0; 


        if (X <= 0) {
            printf("Case #%d: %.7f\n", test, ans); 
            continue; 
        }

        while (money < X) {
            double t1 = (X - money) / v; 
            double t2 = C / v + (X - money) / (v + F); 
            if (t1 <= t2) {
                ans += t1; 
                money = X; 
                break; 
            } else {
                ans += C / v; 
                v += F; 
                money = 0; 
            }
        }

        printf("Case #%d: %.7f\n", test, ans);    
    }   
     
    return 0;  
}
