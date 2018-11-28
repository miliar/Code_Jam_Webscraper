# include <bits/stdc++.h>
using namespace std;
# define N 16
# define J 50
# define sieveSize 100000001

bool sieve[sieveSize]={};
vector <int> prime;
vector <long long> ans;
int divisors[J][10];

int checkComposite(long long num){
    int limit = (int)sqrt(num);
    for (int i=0; i<prime.size() && prime[i]<=limit; i++){
        if (num%prime[i]) continue;
        return prime[i];
    }
    return 0;
}

int main(){
    ///makeSieve
    freopen("Csmallout.txt","w", stdout);
    int limit = (int)sqrt(sieveSize);
    sieve[0] = sieve[1] = true;
    for (int i=2; i<=limit; i++){
        if (sieve[i]) continue;
        prime.push_back(i);
        for (int j=i; i*j<sieveSize; j++) sieve[i*j] = true;
    }
    for (int i=limit+1; i<sieveSize; i++){
        if (sieve[i]) continue;
        prime.push_back(i);
    }
    ///
    int from = 1<<(N-1), to = from<<1;
    long long num, prod;
    //scanf("%lld %lld %lld", &num, &num, &num);    ///Just discard the input, already known
    for (int i=from+1, total=0; i<to && total<J; i+=2){
        bool noPrime = true;
        for (int base=2; base<=10; base++){
            num = 0;
            prod = 1;
            for (int j=0; j<N; j++){
                if ((i&(1<<j))) num += prod;
                prod *= base;
            }
            /// num is now in changed base
            prod = checkComposite(num);
            if (prod) divisors[total][base-2] = prod;
            else{
                noPrime = false;
                break;
            }
        }
        if (noPrime){
            ans.push_back(num);
            total++;
        }
    }
    printf("Case #1:\n");
    for (int i=0; i<J; i++){
        printf("%lld", ans[i]);
        for (int j=0; j<9; j++) printf(" %d", divisors[i][j]);
        printf("\n");
    }
    return 0;
}
