#include<stdio.h>
#include<math.h>
#include<algorithm>
typedef long long ll;

ll divs[9], cnt = 0, printed = 0;
int bin[20];
int N, J;
FILE *fp, *fpo;

bool isPrime(ll num){
    if(num % 2 == 0){
        divs[cnt] = 2;
        return false;
    }
    
    ll to = sqrt(num);
    
    for(int i = 3; i <= to; i += 2){
        if(num % i == 0){
            divs[cnt] = i;
            return false;
        }
    }
    
    return true;
}

ll toDec(ll num, int base){
    ll p = 1, result = 0;
    
    while(num){
        result += (num & 1) * p;
        num >>= 1;
        p *= base;
    }
    
    return result;
}

void nextBin(){
    bin[1]++;
    for(int i = 1; i < N; i++){
        if(bin[i] == 2){
            bin[i] = 0;
            bin[i + 1]++;
        }
    }
}

void printBin(){
    for(int i = N - 1; i >= 0; i--)
        fprintf(fpo, "%d", bin[i]);
    fprintf(fpo, " ");
}

int main(){
    fp = fopen("c.in", "r");
    fpo = fopen("c.out", "w");
    
    int t;
    fscanf(fp, "%d", &t);
    for(int T = 1; T <= t; T++){
        fscanf(fp, "%d%d", &N, &J);
        fprintf(fpo, "Case #1:\n");
        
        ll num = 1 << (N - 1); num++;
        ll to = 1 << N;
        bin[0] = bin[N - 1] = 1;
        while(num <= to - 1 && printed != J){
            for(int i = 2; i <= 10; i++){
                if(!isPrime(toDec(num, i)))
                    cnt++;
                else
                    break;
            }
            
            if(cnt == 9){
                printBin();
                printed++;
                
                for(int i = 0; i < 9; i++){
                    fprintf(fpo, "%lld ", divs[i]);
                }
                fprintf(fpo, "\n");
            }
            
            cnt = 0;
            nextBin();
            num += (1 << 1);
        }
    }
}