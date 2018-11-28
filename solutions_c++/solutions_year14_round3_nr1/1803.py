#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;
typedef long long ll;

ll ObtenirPGCD(ll a, ll b)
{
    if (b == 0)
        return a;
        
    return ObtenirPGCD(b, a % b);
}

void Reduire(ll& num, ll& den)
{
    ll pgcd = ObtenirPGCD(num, den);
    num /= pgcd;
    den /= pgcd;
}

int CompterGeneration(ll& num, ll& den)
{
    int generation = 0;
    
    while (num * 2 < den)
    {
        num *= 2;
        Reduire(num, den);
        generation++;
    }
    
    if (num != den)
        generation++;

    return generation;
}

int CompterGenerationTotal(ll num, ll den)
{
    int totalGenerations = 0;
    int generationPremier = 0;
    int id = 0;
    
    while (totalGenerations <= 40 && num != 0)
    {
        int generationCourante = CompterGeneration(num, den);
    
        if (id == 0)
            generationPremier += generationCourante;
        
        if (num == den)
            break;
        
        totalGenerations += generationCourante;
        num = 2 * num - den;
        Reduire(num, den);
        id++;
    }
    
    return totalGenerations > 40 ? -1 : generationPremier;
}

int main()
{
    int nbTests;
    scanf("%d", &nbTests);
    
    for (int test = 1; test <= nbTests; test++)
    {
        printf("Case #%d: ", test);
        ll num, den;
        scanf("%lld/%lld", &num, &den);
        Reduire(num, den);
        int generation = CompterGenerationTotal(num, den);
        
        if (generation == -1)
            puts("impossible");
        else
            printf("%d\n", generation);
    }
    
    return 0;
}
