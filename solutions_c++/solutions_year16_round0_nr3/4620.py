#include<iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int bin[35];
unsigned long long int n,m,l;
unsigned long long int divisors[12];

unsigned long long int pow_cal(unsigned long long int p, int q){
    unsigned long long temp = 1;
    for(int i=1;i<=q;i++)
         temp *= p;
    return temp;
}

unsigned long long int is_prime(unsigned long long int n)
{
    //if (n == 1) return 0; // 1 is NOT a prime
    if (n == 2) return 1; // 2 is a prime
    if (n%2 == 0) return 2; // NO prime is EVEN, except 2
    for (unsigned long long int i=3; i*i<=n; i+=2) // start from 3, jump 2 numbers
        if (n%i == 0) // no need to check even numbers
            return i;
    return 1;
}

void print_bin(unsigned long long int n,int i){
    if(n==0) return;
    print_bin(n/2,i-1);
    bin[i] = n%2; //printf("%d",n%2);
}

void print_bin(){
    for(int i=1;i<=l;i++){
        printf("%d",bin[i]);
    }
}

unsigned long long int to_any_base(int base){
    unsigned long long int temp = 0,a=l-1,temp2;
    for(int i=1;i<=l;i++){
        temp2 = bin[i]*pow_cal(base,a);
        temp += temp2;
        --a;
    }
    return temp;
}

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    int t,c=0;
    scanf("%d",&t);
    while(t--)
    {
        ++c;
        scanf("%I64d %I64d",&l,&m);
        n = pow_cal(2,l-1) | 1;
        printf("Case #%d:\n",c);
        int j = 0;
        while(j<m){
            print_bin(n,l);
            int flag = 0;
            for(int i=2;i<=10;i++){
                unsigned long long int temp = to_any_base(i);
                temp = divisors[i] = is_prime(temp);
                if(temp == 1){
                    flag = 1;
                    break;
                }
            }

            if(flag==0) {
                print_bin();
                for(int i=2;i<=10;i++){
                    printf(" %I64d",divisors[i]);
                }
                printf("\n");
                ++j;
            }
            n = (n+1) | 1;
        }
    }
    return 0;
}
