#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

vector<int> getJamcoinDivs(ll x)
{
    static vector<int> primes = { 2, 3, 5, 7, 11, 13 };
    vector<int> result;
    
    for (int base = 2; base <= 10; base++)
    {
        for (int prime: primes)
        {
            if (prime >= x) break;
            
            int rest = 0;
            for (int i = 31; i >= 0; i--)
            {
                rest *= base;
                if (x & (1LL << i))
                    rest++;
                rest %= prime;
            }
            
            if (rest == 0)
            {
                result.push_back(prime);
                break;
            }
        }
        
        if ((int)result.size() != base - 1) return vector<int>();
    }
    
    return result;
}

int main()
{
    int nTests;
    scanf("%d", &nTests);
    assert(nTests == 1);
    
    int nDigits, needJamcoins;
    scanf("%d %d", &nDigits, &needJamcoins);
    
    ll now = (1LL << (nDigits - 1)) - 1;
    
    int nGot = 0;
    vector<pair<int, vector<int>>> answer;
    while (nGot < needJamcoins)
    {
        now += 2;
        vector<int> v = getJamcoinDivs(now);
        if (v.empty()) continue;
        
        answer.emplace_back(now, v);
        nGot++;
    }
    
    printf("Case #1:\n");
    for (auto it: answer)
    {
        for (int i = nDigits - 1; i >= 0; i--)
            printf("%d", (it.first & (1LL << i)) ? 1 : 0);
        for (int x: it.second)
            printf(" %d", x);
        printf("\n");
    }
    
    return 0;
}
