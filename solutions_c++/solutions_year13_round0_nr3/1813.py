#include <algorithm>
#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    int T, i, lpos, upos, ret;
    unsigned long long fasr[] = {1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002,10000001,10011001,10100101,10111101,11000011,11011011,11100111,11111111,20000002,100000001,100010001,100020001,100101001,100111001,100121001,101000101,101010101,101020101,101101101,101111101,110000011,110010011,110020011,110101011,110111011,111000111,111010111,111101111,111111111,200000002,200010002};
    vector<unsigned long long> v(fasr, fasr + sizeof(fasr)/sizeof(unsigned long long));

    vector<unsigned long long>::iterator low, up;
    unsigned long long A, B, Ar, Br;
    scanf("%d", &T);
    for (i = 0; i < T; i++)
    {
        scanf("%llu", &A);
        scanf("%llu", &B);
        Ar = (unsigned long long)ceil(sqrt(A));
        Br = (unsigned long long)floor(sqrt(B));
        // printf("Ar = %llu, Br = %llu\n", Ar, Br);
        low = lower_bound(v.begin(), v.end(), Ar);
        up = upper_bound(v.begin(), v.end(), Br);
        lpos = low- v.begin();
        upos = up - v.begin() - 1;
        // printf("Lower bound = %llu, square = %llu\n", v[lpos], v[lpos] * v[lpos]);
        // printf("Upper bound = %llu, square = %llu\n", v[upos], v[upos] * v[upos]);
        ret = (upos < lpos)? 0 : upos-lpos+1;
        printf("Case #%d: %d\n", i + 1, ret);
    }
    return 0;
}
