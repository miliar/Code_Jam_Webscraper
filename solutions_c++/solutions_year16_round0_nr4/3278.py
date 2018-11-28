#include <bits/stdc++.h>

using namespace std;

unsigned long long int power(unsigned long long K , unsigned long long C)
{
    unsigned long long int answer = 1;

    for(unsigned long long int i = 0 ; i < C ; i++)
    {
        answer *= K;
    }
    return answer ;
}

int main()
{
    freopen("D-small-attempt0.in", "r" , stdin);
    freopen("outputSmallD.txt", "w" , stdout);
    unsigned long long int T , K , C , S , range , answer;

    scanf("%llu", &T);

    for(unsigned long long int i = 0 ; i < T ; i++)
    {
        scanf("%llu %llu %llu", &K ,&C , &S);
        range = power(K , C);
        answer = 1;
        printf("Case #%llu:", i+1);
        while(S>0 && range>0)
        {
            printf(" %llu",answer);
            answer++;
            range--;
            S--;
        }
        printf("\n");

    }
    return 0;
}
