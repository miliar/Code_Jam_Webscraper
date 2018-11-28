#include <bits/stdc++.h>
#define cout out
using namespace std;

long long basZ[11], divi[11];

long long lbaza(long long a, long long b)
{
    long long wyn = 0;
    long long x = 0;

    while(b > 0)
    {
        x = x*10 + b%10;
        b /= 10;
    }
    b = x;

    while(b > 0){
        wyn = wyn*a + b%10;
        b/= 10;
    }
    return wyn;
}
int aktualny;
bool isprime(long long a)
{
    if(a < 2) return false;
    for(long long i = 2; i*i <= a; i++){
        if(a%i == 0){
            divi[aktualny] = i;
                return false;
        }
    }
    return true;
}

int main()
{
    ios_base::sync_with_stdio(0);
    ofstream out("C-small-attempt-1.out");
    int t;
    cin >> t;

    int n, k;
    cin >> n >> k;
    int targ = (1 << (n-2))-1;
    long long pom;
    bool all;
    cout << "Case #1:\n";
    for(int i = 0; i <= targ; i++)
    {
        pom = 1;
        for(int j = 0; j < n-2; j++) if((1<<j) & i) pom = pom*10 + 1;
        else pom *= 10;
        all = true;
        pom = pom*10 + 1;
        for(int bazy = 2; bazy <= 10; bazy++)
        {
            aktualny = bazy;
            basZ[bazy] = lbaza(bazy, pom);
            if(isprime(basZ[bazy])){
                all = false;
                break;
            }

        }

        if(all)
        {
            cout << pom << " ";
                for(int w = 2; w <= 10; w++) cout << divi[w] << ' ';
                cout << "\n";
                k--;
        }
        if(k == 0) break;
    }
}
