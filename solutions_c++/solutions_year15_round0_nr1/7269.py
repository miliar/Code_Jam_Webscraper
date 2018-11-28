#include <iostream>
#include <cstdlib>
#include <cmath>
#include <stdio.h>
using namespace std;

int main(){
    FILE *fp;
    fp = fopen("g1.txt","w");
    int T;
    int test_case = 1;
    cin >> T;
    while(T--){
        int Smax;
        int total_stands_up = 0, friends = 0;
        char* audience;
        cin >> Smax;
        audience = new char [Smax+2];
        scanf("%s",audience);
        for(int k = 0;k < Smax+1;k++){
            if(k <= total_stands_up){
                total_stands_up += (audience[k] - '0');
            }else{
                friends += (k - total_stands_up);
                total_stands_up += (k - total_stands_up)+(audience[k] - '0');
            }
        }
        fprintf(fp,"Case #%d: %d\n",test_case,friends);
        test_case++;
    }
    return 0;
}
