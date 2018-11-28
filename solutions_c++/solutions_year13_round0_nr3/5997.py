#include<cstdlib>
#include<cstdio>

unsigned long long tab[10000] = {0,
1,
2,
3,
11,
22,
101,
111,
121,
202,
212,
1001,
1111,
2002,
10001,
10101,
10201,
11011,
11111,
11211,
20002,
20102,
100001,
101101,
110011,
111111,
200002,
1000001,
1001001,
1002001,
1010101,
1011101,
1012101,
1100011,
1101011,
1102011,
1110111,
1111111,
2000002,
2001002};
int indiceMax = 39;

int main()
{
    int nbTest;
    scanf("%d", &nbTest);

    for(int test = 1; test <= nbTest; ++test)
    {
        int A,B;
        scanf("%d%d", &A, &B);
        int tA = 0;
        int tB = 38;
        while(A > tab[tA]*tab[tA])
            tA++;
        while(B < tab[tB]*tab[tB])
            tB--;
        printf("Case #%d: %d\n", test, tB - tA + 1);
        //printf("%d %d\n", tA,tB);
    }
    return 0;
}
