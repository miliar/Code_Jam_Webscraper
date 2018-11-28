#include <iostream>
#include <cstdio>
using namespace std;

long long tab[1000];

int main(){

tab[0] = 1;
tab[1] = 4;
tab[2] = 9;
tab[3] = 121;
tab[4] = 484;
tab[5] = 10201;
tab[6] = 12321;
tab[7] = 14641;
tab[8] = 40804;
tab[9] = 44944;
tab[10] = 1002001;
tab[11] = 1234321;
tab[12] = 4008004;
tab[13] = 100020001;
tab[14] = 102030201;
tab[15] = 104060401;
tab[16] = 121242121;
tab[17] = 123454321;
tab[18] = 125686521;
tab[19] = 400080004;
tab[20] = 404090404;
tab[21] = 10000200001LL;
tab[22] = 10221412201LL;
tab[23] = 12102420121LL;
tab[24] = 12345654321LL;
tab[25] = 40000800004LL;
tab[26] = 1000002000001LL;
tab[27] = 1002003002001LL;
tab[28] = 1004006004001LL;
tab[29] = 1020304030201LL;
tab[30] = 1022325232201LL;
tab[31] = 1024348434201LL;
tab[32] = 1210024200121LL;
tab[33] = 1212225222121LL;
tab[34] = 1214428244121LL;
tab[35] = 1232346432321LL;
tab[36] = 1234567654321LL;
tab[37] = 4000008000004LL;
tab[38] = 4004009004004LL;

    int t;
    long long a, b;
    
    scanf("%d", &t);
    
    for(int i=0; i<t; i++){
        scanf("%lld %lld", &a, &b);    
        
        for(int j=0; j<40; j++){
            if(tab[j] >= a){
                a = j;
                break;    
            }    
        }
        for(int j=38; j>=0; j--){
            if(tab[j] <= b){
                b = j;
                break;    
            }    
        }
        
        printf("Case #%d: %d\n", i+1, max(0LL, b-a+1));
    }
    
    
    return 0;
}
