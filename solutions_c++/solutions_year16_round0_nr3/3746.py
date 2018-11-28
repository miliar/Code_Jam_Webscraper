#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<memory.h>
#include<map>
#include<string>
using namespace std;


int dp[101][2];


long long get_divisor(long long n){
    if( n <= 2){
        return -1;
    }else if( n %2 == 0){
        return 2;
    }
    
    for(long long divisor = 3; divisor * divisor < n; divisor +=2){
        if( n % divisor == 0){
            return divisor;
        }
    }
    return -1;
}
void test_case()
{
    int n, j;
    cin >> n >> j;

    for(long long mid = 0 ; j > 0 ; mid ++){
        long long bits = (mid<<1) | 1 | ( 1 << (n-1));
        vector<long long> divisors(11, -1);
        bool sw = true;
        for(long long base = 2; base <= 10; base ++){
            long long digit = 1;
            long long val = 0;
            for(int i = 0 ; i < n; i++, digit *= base){
                if( ( ( 1 << i ) & bits ) > 0 ){
                    val += digit;
                }
            }
            
            divisors[base] = get_divisor(val);
            if(divisors[base] == -1){
                sw = false;
                break;
            }
        }
        if(sw){
            j--;
            for(int i = n-1 ; i >=0 ; i--){
                if( ( ( 1 << i ) & bits ) > 0 ){
                    printf("1");
                }else{
                    printf("0");
                }
            }
            for(int base = 2; base <= 10; base ++){
                printf(" %d", divisors[base]);
            }
            printf("\n");
        }
        
    }
    
}
int main(){
    freopen("/Users/waps12b/Downloads/C-small-attempt0.in","r",stdin);
    freopen("/Users/waps12b/Downloads/out.txt","w+",stdout);
    
    int t;
    scanf("%d",&t);
    for(int i = 1; i<= t; i++){
        printf("Case #%d:\n", i);
        test_case();
    }
    
    return 0;
}